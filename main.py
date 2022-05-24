import pygame
from pygame.sprite import Group
from stats import Stats
import controls
from enemy import Enemy
from rocket import Rocket
from wall import Wall


def create_walls(screen):
    walls = Group()
    walls.add(Wall(screen, 100, 100))
    walls.add(Wall(screen, 100, 132))
    return walls


def run():
    countEnemies = 0
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game")
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
            pass
        else:
            if len(enemies) < 7:
                if pygame.time.get_ticks() % 1000 == 0:
                    enemies.add(Enemy(screen, walls, enemies))
            controls.events(screen, rocket, bullets)
            rocket.update_rocket(walls, enemies)
            controls.update(bg_color, screen, rocket, walls, bullets,enemybullets, enemies, stats)


run()
