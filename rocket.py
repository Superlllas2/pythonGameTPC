import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):

    def __init__(self, screen):
        """Player init"""
        super(Rocket, self).__init__()

        self.sprites = []
        # self.image = pygame.image.load('Resources/Pictures/Character/rocket2.png')
        self.sprites.append(pygame.image.load('Resources/Pictures/Character/rocket2.png'))
        self.sprites.append(pygame.image.load('Resources/Pictures/Character/rocket1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


        self.screen = screen
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
        """Player output"""
        self.screen.blit(self.image, self.rect)

    def update_rocket(self, walls, enemies, stats):
        """Player position update"""
        x = self.x
        y = self.y
        if self.mright and self.rect.right < self.screen_rect.right:
            self.x += 0.5
        if self.mleft and self.rect.left > 0:
            self.x -= 0.5
        if self.mup and self.rect.top > 0:
            self.y -= 0.5
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += 0.5
        self.rect.centerx = self.x
        self.rect.centery = self.y
        collisions = pygame.sprite.spritecollide(self, walls, False)
        if collisions:
            self.rect.centerx = x
            self.rect.centery = y
            self.x = x
            self.y = y
        collisions = pygame.sprite.spritecollide(self, enemies, True)
        if collisions:
            self.rect.centerx = x
            self.rect.centery = y
            self.x = x
            self.y = y
            stats.hp_left -= 1

        """Player animation"""
        # self.current_sprite += 1
        # self.image = self.sprites[self.current_sprite]

    def create_rocket(self):
        """Player position"""
        self.y = 500
        self.x = 500

    def get_coor(self):
        return self.rect.centerx, self.rect.centery
