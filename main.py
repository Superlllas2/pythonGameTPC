import pygame, controls
from rocket import Rocket
from wall import Wall
from pygame.sprite import Group


def create_walls(screen):
    walls = Group()
    walls.add(Wall(screen, 100, 100))
    walls.add(Wall(screen, 100, 132))
    return walls


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("игра")
    bg_color = (100, 100, 200)
    rocket = Rocket(screen)
    rocket.create_rocket()
    bullets = Group()
    enemies = Group()
    walls = create_walls(screen)

    while True:
        controls.events(screen, rocket)
        rocket.update_rocket(walls)
        controls.update(bg_color, screen, rocket, walls)


run()
