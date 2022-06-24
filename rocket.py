import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    def __init__(self, screen):
        """Player init"""
        super(Rocket, self).__init__()

        """Animation"""
        self.is_running = False
        self.current_sprite = 0

        self.spritesR = []
        self.spritesR.append(pygame.image.load('Resources/Pictures/Character/LookingRight/RocketLookingRight.png'))
        self.spritesR.append(pygame.image.load('Resources/Pictures/Character/LookingRight/RocketLookingRight1.png'))
        self.spritesR.append(pygame.image.load('Resources/Pictures/Character/LookingRight/RocketLookingRight2.png'))
        self.spritesR.append(pygame.image.load('Resources/Pictures/Character/LookingRight/RocketLookingRight3.png'))

        self.spritesL = []
        self.spritesL.append(pygame.image.load('Resources/Pictures/Character/LookingLeft/RocketLookingLeft.png'))
        self.spritesL.append(pygame.image.load('Resources/Pictures/Character/LookingLeft/RocketLookingLeft1.png'))
        self.spritesL.append(pygame.image.load('Resources/Pictures/Character/LookingLeft/RocketLookingLeft2.png'))
        self.spritesL.append(pygame.image.load('Resources/Pictures/Character/LookingLeft/RocketLookingLeft3.png'))

        self.image = self.spritesR[self.current_sprite]

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
            self.x += 1
        if self.mleft and self.rect.left > 0:
            self.x -= 1
        if self.mup and self.rect.top > 0:
            self.y -= 1
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1
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
        if self.is_running:
            # Part of code to make an animation for a running character
            # Right now is just the same as if he stands still
            if pygame.mouse.get_pos()[0] > x:
                self.image = self.spritesR[int(self.current_sprite)]
                self.current_sprite += 0.04
                if self.current_sprite >= len(self.spritesR):
                    self.current_sprite = 0
                self.image = self.spritesR[int(self.current_sprite)]
            else:
                self.image = self.spritesL[int(self.current_sprite)]
                self.current_sprite += 0.04
                if self.current_sprite >= len(self.spritesL):
                    self.current_sprite = 0
                self.image = self.spritesL[int(self.current_sprite)]
        else:
            if pygame.mouse.get_pos()[0] > x:
                self.image = self.spritesR[int(self.current_sprite)]
                self.current_sprite += 0.04
                if self.current_sprite >= len(self.spritesR):
                    self.current_sprite = 0
                self.image = self.spritesR[int(self.current_sprite)]
            else:
                self.image = self.spritesL[int(self.current_sprite)]
                self.current_sprite += 0.04
                if self.current_sprite >= len(self.spritesL):
                    self.current_sprite = 0
                self.image = self.spritesL[int(self.current_sprite)]

    def animate_run(self):
        self.is_running = True

    def create_rocket(self):
        """Player position"""
        self.y = 500
        self.x = 500

    def get_coor(self):
        return self.rect.centerx, self.rect.centery
