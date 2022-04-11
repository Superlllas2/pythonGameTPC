import pygame
from Tiles import Tile, StaticTile
from Settings import tile_size
from LevelSupport import import_csv_layout, import_cut_graphics


class Level:
    def __init__(self, level_data, surface):
        # General setup
        self.display_surface = surface
        self.world_shift = -5

        # Terrain set up
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

    def create_tile_group(self, layout, layer):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if layer == 'terrain':
                        terrain_tile_list = import_cut_graphics('Resources/Pictures/Background/Ground.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)
        return sprite_group

    def run(self):
        # Runs the entire game / level
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
