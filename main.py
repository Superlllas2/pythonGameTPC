import pygame
from pygame.sprite import Group, Sprite
from stats import Stats
import controls
from enemy import Enemy
from rocket import Rocket
from wall import Wall


def create_walls(screen):
    walls = Group()
    x, y = screen.get_size()
    for i in range(x // 32 + 1):
        walls.add((Wall(screen, i * 32, 0)))
        walls.add((Wall(screen, i * 32, y - 32)))
    for i in range(y // 32 + 1):
        walls.add((Wall(screen, 0, i * 32)))
        walls.add((Wall(screen, x - 32, i * 32)))
    return walls


def run():
    pygame.init()
    screen = pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0)
    pygame.display.set_caption("Game")
    wasted = Sprite()
    wasted.image = pygame.image.load('Resources/Pictures/Character/wasted.png')
    wasted.screen = screen
    bg_color = (100, 100, 200)
    rocket = Rocket(screen)
    rocket.create_rocket()
    bullets = Group()
    enemybullets = Group()
    enemies = Group()
    walls = create_walls(screen)
    stats = Stats()
    b = True
    while b:
        if stats.hp_left <= 0:
            wasted.screen.blit(wasted.image, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.display.quit()
                    b = False
        else:
            if len(enemies) < 7:
                if pygame.time.get_ticks() % 50 == 0:
                    enemies.add(Enemy(screen, walls, enemies))
            controls.events(screen, rocket, bullets, stats)
            rocket.update_rocket(walls, enemies, stats)
            controls.update(bg_color, screen, rocket, walls, bullets, enemybullets, enemies, stats)


run()
