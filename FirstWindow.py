import pygame
from pygame.locals import *


class GameWindow:
    # Initiates the pygame library. THIS LINE IS NEEDED IN EVERY NEW CLASS!!!
    pygame.init()

    # Setting up the screen size
    screen_width = 220
    screen_height = 183

    # Setting up the window with dimensions and its caption
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    # Setting up the picture to use
    backgroundImg = pygame.image.load('Resources/Pictures/Background/Trololo.png')

    # Draw one image onto another. In our case it is drawing the Trololo image onto literally nothing
    screen.blit(backgroundImg, (0, 0))


