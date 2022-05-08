import pygame
from pygame.sprite import Sprite
from math import sqrt


class Bullet(Sprite):
    def __init__(self, screen, h_x, h_y, m_x, m_y):
        """инициализация пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/bullet.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = h_x
        self.rect.centery = h_y-50
        self.x = h_x
        self.y = h_y
        d = sqrt((h_x - m_x) ** 2 + (h_y - m_y) ** 2)
        self.d_y = 0.2 / d * (h_y - m_y)  # изменение координат
        self.d_x = 0.2 / d * (h_x - m_x)

    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)

    def update_bullet(self):
        """обновление позиции игрока"""
        self.x -= self.d_x
        self.y -= self.d_y
        self.rect.centerx = self.x
        self.rect.centery = self.y