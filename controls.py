import pygame, sys
from bullet import Bullet


def events(screen, rocket, bullets):
    """Parsing pressed key"""
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            h_x, h_y = rocket.get_coor()
            bullets.add(Bullet(screen, h_x, h_y, mouse_pos[0], mouse_pos[1]))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                rocket.mright = False
            elif event.key == pygame.K_a:
                rocket.mleft = False
            elif event.key == pygame.K_s:
                rocket.mdown = False
            elif event.key == pygame.K_w:
                rocket.mup = False

def update_bullets(screen,rocket, enemies, walls, bullets,enemybullets,stats):
    """Updating bullets positions"""
    bullets.update()
    for bullet in bullets.sprites():
        bullet.update_bullet()
    for bullet in enemybullets.sprites():
            bullet.update_bullet()
    for bullet in bullets.copy():
        if bullet.rect.centerx <= 0 or bullet.rect.centerx > 800:
            bullets.remove(bullet)
        if bullet.rect.centery <= 0 or bullet.rect.centery > 600:
            bullets.remove(bullet)
    for bullet in enemybullets.copy():
        if bullet.rect.centerx <= 0 or bullet.rect.centerx > 800:
            enemybullets.remove(bullet)
        if bullet.rect.centery <= 0 or bullet.rect.centery > 600:
            enemybullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, walls, True, False)
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    collisions = pygame.sprite.spritecollide(rocket, enemybullets, True)
    if collisions:
        stats.hp_left -= 1


def update(bg_color, screen, rocket, walls, bullets,enemybullets, enemies,stats):
    """Screen update"""
    screen.fill(bg_color)
    update_bullets(screen,rocket, enemies, walls, bullets,enemybullets,stats)
    if pygame.time.get_ticks() % 1000 == 0:
        for i in enemies:
            enemybullets.add(Bullet(screen, i.rect.centerx,i.rect.centery, rocket.x, rocket.y))
    for i in walls:
        i.output()
    for i in bullets:
        i.output()
    for i in enemies:
        i.output()
    for i in enemybullets:
        i.output()
    rocket.output()
    pygame.display.flip()
