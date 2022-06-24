import pygame
from pygame.sprite import Sprite
from math import sqrt


class Bullet(Sprite):
    def __init__(self, screen, h_x, h_y, m_x, m_y):
        """Bullet init"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Resources/Pictures/Character/Bullet3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = h_x
        self.rect.centery = h_y-32
        self.x = h_x
        self.y = h_y
        d = sqrt((h_x - m_x) ** 2 + (h_y-32 - m_y) ** 2)
        self.d_y = 1 / d * (h_y-32 - m_y)    # coordinates change
        self.d_x = 1 / d * (h_x - m_x)

    def output(self):
        """Showing the bullet"""
        self.screen.blit(self.image, self.rect)

    def update_bullet(self):
        """Bullet position update"""
        self.x -= self.d_x
        self.y -= self.d_y
        self.rect.centerx = self.x
        self.rect.centery = self.y
