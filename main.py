# this allows us to use code from
# the open-source pygame library
# throughout this file
# 1- import pygame at the top of the main() function
import pygame
from constants import *

def main():
    #initialize the pygame
    pygame.init()
    print("Starting Asteroids!")
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # 4 - Use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create the game loop. For now, we'll only worry about step 3: drawing the game onto the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit the game loop and end the program
        #se the screen's fill method to fill the screen with a solid "black" color.
        screen.fill((0, 0, 0))

        #Use pygame's display.flip() method to refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

