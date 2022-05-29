import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self,screen,x,y):
        super(Wall, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Background/wall1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centerx = x+16
        self.rect.centery = y+16

    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)