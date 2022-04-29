import pygame
import math

# 1. Write code for collision use the algebric midpoint
# 2. Write code for bullet
# 3. Create the wall which rocket can't pass
# 4. Add physics of inertion, stopping is too fast
# 5. Write the classes for player

pygame.init()
running = True
screen = pygame.display.set_mode((800, 600))

rocketIMG = pygame.image.load('Resources/Pictures/Character/rocket.png')
rocketX = 270
rocketY = 250
r_changeX = 0
r_changeY = 0

# Rocket2
ufoIMG = pygame.image.load('Resources/Pictures/Background/ufo.png')
ufoX = 470
ufoY = 250
u_changeX = 0
u_changeY = 0

# Wall
wall_img = pygame.image.load('Resources/Pictures/Background/Ground.png')
wallX = 64
wallY = 250


class Rocket(pygame.sprite.Sprite):

    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = surface

        self.rect = self.image.get_rect() # size and position


def rocket_load(r_x, r_y):
    screen.blit(rocketIMG, (r_x, r_y))


def ufo_load(u_x, u_y):
    screen.blit(ufoIMG, (u_x,u_y))


def wall_load(w_x,w_y):
    screen.blit(wall_img, (w_x,w_y))


def isCollision(rocketX, rocketY, ufoX, ufoY):
    d = math.sqrt((math.pow(rocketX - ufoX,2)) + (math.pow(rocketY - ufoY,2)))
    if d < 64:
        return True
    else:
        return False


def isWall(rocketX, rocketY, wallX, wallY):
    d = math.sqrt((math.pow(rocketX - wallX, 2)) + (math.pow(rocketY - wallY, 2)))
    if d < 96:
        if rocketX < wallX:
            return 1
        elif rocketX > wallX:
            return 2
        elif rocketY < wallY:
            return 3
        elif rocketY > wallY:
            return 4
    else:
        return 0


while running:
    screen.fill((100, 100, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ufo movement keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                u_changeX = -0.4
            if event.key == pygame.K_RIGHT:
                u_changeX = 0.4
            if event.key == pygame.K_UP:
                u_changeY = -0.4
            if event.key == pygame.K_DOWN:
                u_changeY = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                u_changeX = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                u_changeY = 0

        # Rocket movement keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                r_changeX = -0.4
            if event.key == pygame.K_d:
                r_changeX = 0.4
            if event.key == pygame.K_w:
                r_changeY = -0.4
            if event.key == pygame.K_s:
                r_changeY = 0.4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or pygame.K_a:
                r_changeX = 0
            if event.key == pygame.K_w or pygame.K_s:
                r_changeY = 0

    # Boarders of ufo
    if ufoX <= 0:
        ufoX = 0
    elif ufoX >= 736:
        ufoX = 736
    if ufoY <= 0:
        ufoY = 0
    elif ufoY >= 536:
        ufoY = 536

    # Boarders of rocket
    if rocketX <= 0:
        rocketX = 0
    elif rocketX >= 736:
        rocketX = 736

    if rocketY <= 0:
        rocketY = 0
    elif rocketY >= 536:
        rocketY = 536

    # Cohesion
    if ufoX == rocketX and ufoY == rocketY:
        ufoX -= +20
        rocketX -= -20

    d = math.sqrt(((ufoX-rocketX)**2)+ ((ufoY-rocketY)**2))
    if d <= 64:
        rocketX -= 10
        rocketY += 10
        ufoX += 10
        ufoY -= 10

    # Collision
    collision = isCollision(rocketX, rocketY, ufoX, ufoY)
    if collision:
        rocketX -= 10
        rocketY += 10
        ufoX += 10
        ufoY -= 10

    # wallCall = isWall(rocketX, rocketY, wallX, wallY)
    # if wallCall != 0:
        # if wallCall == 1:
        #     rocketX = wallX - 96
        # if wallCall == 2:
        #     rocketX = wallX + 96
        # if wallCall == 3:
        #     rocketY = wallY - 96
        # if wallCall == 4:
        #     rocketY = wallY + 96
    rocket = Rocket(rocketIMG)
    wall = Rocket(wall_img)
    if pygame.sprite.spritecollide(rocket, pygame.sprite.AbstractGroup(wall), False):
        print("Collision")


    ufoX += u_changeX
    ufoY += u_changeY
    rocketX += r_changeX
    rocketY += r_changeY

    # Functions for running
    wall_load(wallX, wallY)
    rocket_load(rocketX, rocketY)
    ufo_load(ufoX, ufoY)
    pygame.display.update()

