import pygame, sys
from pygame.locals import *
import os
from PIL import Image


class StartUpWindow():
    # dirname = os.path.dirname(__file__)

    pygame.init()
    flags = pygame.OPENGL
    DISPLAYSURF = pygame.display.set_mode((400, 300), flags, vsync=1)
    pygame.display.set_caption('The Game')
    # test
    # WHITE = (255, 255, 255)
    # catImg = pygame.image.load((os.path.join(dirname, 'Resources/Pictures/Background/ToiletMan.png')))
    # Image.open(os.path.join(dirname, 'Resources/Pictures/Background/ToiletMan.png'))
    # catx = 10
    # caty = 10
    # direction = 'right'


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.set_mode()
