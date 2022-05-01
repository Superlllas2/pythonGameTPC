
import pygame, controls
from rocket import Rocket
from wall import Wall
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("игра")
    bg_color = (100, 100, 200)
    rocket = Rocket(screen)
    rocket.create_rocket()
    wall=Wall(screen)
    wall.create_wall()
    while True:
        controls.events(screen, rocket)
        rocket.update_rocket()
        controls.update(bg_color, screen, rocket,wall)

run()
