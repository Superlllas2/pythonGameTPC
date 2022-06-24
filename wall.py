import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    """Wall init"""

    def __init__(self, screen, x, y):
        super(Wall, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Background/wall.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centerx = x + 16
        self.rect.centery = y + 16

    def output(self):
        """Wall being updated"""
        self.screen.blit(self.image, self.rect)
