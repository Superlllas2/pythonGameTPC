import pygame
from pygame.sprite import Group

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
    enemies = Group()
    walls = create_walls(screen)

    while True:
        # if pygame.time.get_ticks() % 1000 == 0:
        if countEnemies < 7:
            if pygame.time.get_ticks() % 1000 == 0:
                enemies.add(Enemy(screen))
                countEnemies += 1

        controls.events(screen, rocket, bullets)
        rocket.update_rocket(walls)
        controls.update(bg_color, screen, rocket, walls, bullets, enemies)


run()
