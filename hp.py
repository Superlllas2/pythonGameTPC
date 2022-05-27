import pygame
from pygame.sprite import Sprite


class Hp(Sprite):

    def __init__(self, screen):
        """Player init"""
        super(Hp, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Character/hp.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx =785
        self.rect.centery = 15

    def output(self, stats):
        """Player output"""
        self.rect.centerx = 785
        self.rect.centery = 15
        for i in range (stats.hp_left):
            self.screen.blit(self.image, self.rect)
            self.rect.centerx -=20
