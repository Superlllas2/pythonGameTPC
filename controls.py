import pygame, sys
from rocket import Rocket


def events(screen, rocket):
    """обработка нажатий клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                rocket.mright = True
            elif event.key == pygame.K_a:
                rocket.mleft = True
            elif event.key == pygame.K_s:
                rocket.mdown = True
            elif event.key == pygame.K_w:
                rocket.mup = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                rocket.mright = False
            elif event.key == pygame.K_a:
                rocket.mleft = False
            elif event.key == pygame.K_s:
                rocket.mdown = False
            elif event.key == pygame.K_w:
                rocket.mup = False


def update(bg_color, screen, rocket,wall):
    """обновление экрана"""
    screen.fill(bg_color)
    wall.output()
    rocket.output()
    pygame.display.flip()
