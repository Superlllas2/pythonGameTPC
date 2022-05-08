import random

import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/enemy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx =self.x = random.randrange(0,800)
        self.rect.centery =self.y = random.randrange(0,600)

    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)


    def create_enemy(self):
        """размещение пушки"""
        self.y = random.randrange(0,600)
        self.x = random.randrange(0,800)