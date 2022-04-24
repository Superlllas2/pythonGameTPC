import sys
import pygame
import Settings
from level import Level
from GameData import level_0


if __name__ == "__main__":
    pygame.init()

    # Setting up the window with dimensions and its caption
    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    pygame.display.set_caption('TPC Game')

    clock = pygame.time.Clock()
    level = Level(level_0, screen)

    # Movement setup
    movement_speed = 2
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False

    # While is always True, which will run the code endlessly, until we quit the game
    while True:
        # Logic which stops the game when pressed close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #         moving_right = True
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            #         moving_left = True
            #     if event.key == pygame.K_UP or event.key == pygame.K_w:
            #         moving_up == True
            #     if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            #         moving_down = True
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #         moving_right = False
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            #         moving_left = False
            #     if event.key == pygame.K_UP or event.key == pygame.K_w:
            #         moving_up = False
            #     if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            #         moving_down = False
        screen.fill('black')
        # We start the game
        level.run()
        # Literally updates the screen = FPS
        pygame.display.update()
        clock.tick(60)
