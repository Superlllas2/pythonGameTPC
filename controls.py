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

    def update_bullets(screen, enemies,walls, bullets):
        """обновление позиции пуль"""
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(bullets, walls, True, False)
        collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)

        # if collisions:
        #     for inos in collisions.values():
        #         stats.score += 10 * len(inos)
        #     sc.image_score()
        #     check_high_score(stats, sc)
        #     sc.image_guns()
        # if len(inos) == 0:
        #     bullets.empty()
        #     create_army(screen, inos)
def update(bg_color, screen, rocket,walls):
    """обновление экрана"""
    screen.fill(bg_color)
    for i in walls:
        i.output()
    rocket.output()
    pygame.display.flip()
