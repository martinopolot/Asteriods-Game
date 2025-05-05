# this allows us to use code from
# the open-source pygame library
# throughout this file
# 1- import pygame at the top of the main() function
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    #initialize the pygame
    pygame.init()

    # print("Starting Asteroids!")
    
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    # 4 - Use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   # create player at the center of the screen
    # player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # create pygame.time.Clock object
    clock = pygame.time.Clock()
    # dt variable set to 0
     # create two main groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # create asteriods group
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set container static field
    Asteroid.containers = (asteriods, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    #set AsteriodField to only update group
    AsteroidField.containers = updatable

    # create asteriods
    # asteriod1 = Asteroid(100, 100, 30)
    # asteriod2 = Asteroid(300, 200, 40)
    asteriod_field = AsteroidField()
    # create asteriod field
    # asteriod_field = AsteroidField(10, SCREEN_WIDTH, SCREEN_HEIGHT)

    # set static containers for a Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
   
    #Create the game loop. For now, we'll only worry about step 3: drawing the game onto the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit the game loop and end the program
    
        # player.update(dt) # update the screen
        updatable.update(dt)

        # collision detection - Player vs Asteriod

        for asteriod in asteriods:
            if asteriod.collides_with(player):
                print("Game over!")
                # pygame.quit()
                sys.exit()
        # collision: Shot vs Asteriod
            for shot in shots:
                if asteriod.collides_with(shot):
                    shot.kill()
                    # asteriod.kill()
                    asteriod.split()
        #se the screen's fill method to fill the screen with a solid "black" color.
        screen.fill((0, 0, 0))
        # screen.fill("black")
        # draw the player

        for obj in drawable:
            obj.draw(screen)
        # player.draw(screen)

        """Expected Behavior:
            Press A to rotate left (counter-clockwise).
            Press D to rotate right (clockwise).
            Rotation speed is smooth and frame-rate independent.
        """

        #Use pygame's display.flip() method to refresh the screen
        pygame.display.flip()
        
        #call the .tick() method and pass it 60- it will pause the game loop until 1/60th of a second has passed.
        dt = clock.tick(60) / 1000 # convert ms to seconds
        # the above limits the framerate to 60 FPS
if __name__ == "__main__":
    main()

