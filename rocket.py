import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Rocket, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Character/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centerx)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)

    def update_rocket(self):
        """обновление позиции игрока"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.x += 0.5
        if self.mleft and self.rect.left > 0:
            self.x -= 0.5
        if self.mup and  self.rect.top > 0:
            self.y -= 0.5
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += 0.5
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def create_rocket(self):
        """размещение пушки по центру внизу экрана"""
        self.y = self.screen_rect.centery
        self.x = self.screen_rect.centerx
