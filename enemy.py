import random
import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, walls, enemies):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Character/Enemy2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.x = random.randrange(32, screen.get_size()[0])
        self.rect.centery = self.y = random.randrange(32, screen.get_size()[1])
        while pygame.sprite.spritecollide(self, walls, False) or pygame.sprite.spritecollide(self, enemies, False):
            self.rect.centerx = self.x = random.randrange(32, screen.get_size()[0])
            self.rect.centery = self.y = random.randrange(32, screen.get_size()[1])

    def output(self):
        """Enemy sprite drawing"""
        self.screen.blit(self.image, self.rect)

    def create_enemy(self):
        """Setting the coordinates for enemies to spawn"""
        self.y = random.randrange(0, 600)
        self.x = random.randrange(0, 800)
