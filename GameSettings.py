import pygame
from Level import Level
from GameData import level_0


class GameWindow:
    # Initiates the pygame library. THIS LINE IS NEEDED IN EVERY NEW CLASS WHERE PYGAME IS USED!!!
    pygame.init()

    vertical_tile_number = 20
    tile_size = 32

    # Setting up the screen size
    screen_height = vertical_tile_number * tile_size
    screen_width = 1200

    # Setting up the window with dimensions and its caption
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    level = Level(level_0, screen)
