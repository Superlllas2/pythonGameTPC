import sys
import pygame
import Settings
from level import Level
from GameData import level_0


if __name__ == "__main__":
    pygame.init()

    # Setting up the window with dimensions and its caption
    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    pygame.display.set_caption('Platformer')

    clock = pygame.time.Clock()
    level = Level(level_0, screen)

    # While is always True, which will run the code endlessly, until we quit the game
    while True:
        # Logic which stops the game when pressed close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        # We start the game
        level.run()
        # Literally updates the screen = FPS
        pygame.display.update()
        clock.tick(60)
