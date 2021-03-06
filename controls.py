import random
from threading import Thread

import pygame
import sys

from bullet import Bullet
from hp import Hp


def events(screen, rocket, bullets, stats):
    """Parsing pressed key"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                rocket.is_running = True
                rocket.mright = True
            elif event.key == pygame.K_a:
                rocket.is_running = True
                rocket.mleft = True
            elif event.key == pygame.K_s:
                rocket.is_running = True
                rocket.mdown = True
            elif event.key == pygame.K_w:
                rocket.is_running = True
                rocket.mup = True
            elif event.key == pygame.K_r:
                mouse_pos = pygame.mouse.get_pos()
                h_x, h_y = rocket.get_coor()
                t1 = Thread(target=wait, args=("reload", stats, True, screen, bullets, h_x, h_y, mouse_pos))
                t1.start()
                sound("reload")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            h_x, h_y = rocket.get_coor()
            if stats.bulletsNum > 0:
                sound("shooting")
                if rocket.mright or rocket.mleft or rocket.mdown or rocket.mup:
                    t2 = Thread(target=wait, args=("shooting", stats, True, screen, bullets, h_x, h_y, mouse_pos))
                    t2.start()
                else:
                    t3 = Thread(target=wait, args=("shooting", stats, True, screen, bullets, h_x, h_y, mouse_pos))
                    t3.start()
                stats.bulletsNum -= 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                rocket.is_running = False
                rocket.mright = False
            elif event.key == pygame.K_a:
                rocket.is_running = False
                rocket.mleft = False
            elif event.key == pygame.K_s:
                rocket.is_running = False
                rocket.mdown = False
            elif event.key == pygame.K_w:
                rocket.is_running = False
                rocket.mup = False


def shooting(running, screen, bullets, h_x, h_y, mouse_pos):
    if running:
        bullets.add(Bullet(screen, h_x, h_y, (mouse_pos[0] + random.randrange(-50, 50)),
                           (mouse_pos[1] + random.randrange(-50, 50))))
    else:
        bullets.add(Bullet(screen, h_x, h_y, (mouse_pos[0] + random.randrange(-15, 15)),
                           (mouse_pos[1] + random.randrange(-15, 15))))


def wait(eventHappens, stats, running, screen, bullets, h_x, h_y, mouse_pos):
    if eventHappens == "reload":
        pygame.time.wait(3100)
        stats.bulletsNum = 30
    elif eventHappens == "shooting":
        pygame.time.wait(10)
        shooting(running, screen, bullets, h_x, h_y, mouse_pos)


def sound(sound):
    shootingSound = pygame.mixer.Sound('Resources/SFX/gunfiresound.mp3')
    reloadSound = pygame.mixer.Sound('Resources/SFX/reload.mp3')
    deadAllien = pygame.mixer.Sound('Resources/SFX/allienIsDead.mp3')
    if sound == "shooting":
        shootingSound.play()
    elif sound == "reload":
        reloadSound.play()
    elif sound == "kill":
        deadAllien.play()


def update_bullets(screen, rocket, enemies, walls, bullets, enemybullets, stats):
    """Updating bullets positions"""
    bullets.update()
    for bullet in bullets.sprites():
        bullet.update_bullet()
    for bullet in enemybullets.sprites():
        bullet.update_bullet()
    for bullet in bullets.copy():
        if bullet.rect.centerx <= 0 or bullet.rect.centerx > screen.get_size()[0]:
            bullets.remove(bullet)
        if bullet.rect.centery <= 0 or bullet.rect.centery > screen.get_size()[1]:
            bullets.remove(bullet)
    for bullet in enemybullets.copy():
        if bullet.rect.centerx <= 0 or bullet.rect.centerx > screen.get_size()[0]:
            enemybullets.remove(bullet)
        if bullet.rect.centery <= 0 or bullet.rect.centery > screen.get_size()[1]:
            enemybullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, walls, True, False)
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for i in collisions:
        stats.score += 10
        sound("kill")
    collisions = pygame.sprite.groupcollide(enemybullets, walls, True, False)
    collisions = pygame.sprite.spritecollide(rocket, enemybullets, True)
    if collisions:
        stats.hp_left -= 1


def update(bg_color, screen, rocket, walls, bullets, enemybullets, enemies, stats):
    """Screen update"""
    screen.fill(bg_color)
    f1 = pygame.font.Font(None, 36)  # Font set up
    text2 = f1.render(str(stats.score), False, (0, 0, 0))
    text3 = f1.render(str(stats.bulletsNum), False, (0, 0, 0))
    update_bullets(screen, rocket, enemies, walls, bullets, enemybullets, stats)
    if pygame.time.get_ticks() % 500 == 0:
        for i in enemies:
            enemybullets.add(Bullet(screen, i.rect.centerx, i.rect.centery, rocket.x, rocket.y))
    for i in walls:
        i.output()
    for i in bullets:
        i.output()
    for i in enemies:
        i.output()
    for i in enemybullets:
        i.output()
    rocket.output()
    hp = Hp(screen)
    hp.output(stats)
    screen.blit(text2, (10, 10))
    screen.blit(text3, (screen.get_size()[0] - len(str(stats.bulletsNum)) * 18 - 45, screen.get_size()[1] - 65))
    pygame.display.flip()
