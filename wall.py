import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self,screen):
        super(Wall, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Background/Ground.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    def create_wall(self):
        """размещение пушки по центру внизу экрана"""
        self.rect.centerx = 200
        self.rect.centery = 200
    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)