import pygame
from pygame.locals import *
from Level import Level
from GameData import level_0


class GameWindow:
    vertical_tile_number = 20
    tile_size = 32

    # Setting up the screen size
    screen_height = vertical_tile_number * tile_size
    screen_width = 1200

    # Setting up the window with dimensions and its caption
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    level = Level(level_0, screen)

    # Initiates the pygame library. THIS LINE IS NEEDED IN EVERY NEW CLASS!!!
    pygame.init()

    # Setting up the picture to use
    backgroundImg = pygame.image.load('Resources/Pictures/Background/Trololo.png')

    # Draw one image onto another. In our case it is drawing the Trololo image onto literally nothing
    screen.blit(backgroundImg, (0, 0))