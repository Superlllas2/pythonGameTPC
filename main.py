import pygame
from pygame.sprite import Group, Sprite
from stats import Stats
import controls
from enemy import Enemy
from rocket import Rocket
from wall import Wall


def create_walls(screen):
    walls = Group()
    walls.add(Wall(screen, 100, 100))
    walls.add(Wall(screen, 100, 132))
    walls.add(Wall(screen,300,300))
    return walls


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game")
    wasted = Sprite()
    wasted.image = pygame.image.load('Resources/Pictures/Character/wasted.jpg')
    wasted.screen = screen
    bg_color = (100, 100, 200)
    rocket = Rocket(screen)
    rocket.create_rocket()
    bullets = Group()
    enemybullets=Group()
    enemies = Group()
    walls = create_walls(screen)
    stats = Stats()
    while True:
        if stats.hp_left<0:
            wasted.screen.blit(wasted.image, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.display.quit()
                    break
        else:
            if len(enemies) < 7:
                if pygame.time.get_ticks() % 1000 == 0:
                    enemies.add(Enemy(screen, walls, enemies))
            controls.events(screen, rocket, bullets)
            rocket.update_rocket(walls, enemies,stats)
            controls.update(bg_color, screen, rocket, walls, bullets,enemybullets, enemies, stats)

run()
