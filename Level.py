import pygame
from LevelSupport import import_csv_layout


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        terrain_layout = import_csv_layout(level_data['terrain'])

    def run(self):
        pass

