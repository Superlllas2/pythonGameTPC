import pygame
import FirstWindow
if __name__ == "__main__":

    # Boolean statement in order to run the code unless we equate it to False
    run = True

    # While run is True, which is the case
    while run:
        # We call the class which starts the window
        FirstWindow.GameWindow()
        # Logic which stops the game when pressed close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Literally updates the screen = FPS
        pygame.display.update()
    pygame.quit()
