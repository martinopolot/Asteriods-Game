Game Loop

Video games are generally built using a game loop. The simplest game loop has 3 steps:

    Check for player inputs
    Update the game world
    Draw the game to the screen

To create a good user experience, these 3 steps need to happen many times per second.
Assignment

    import pygame at the top of your main.py file. The pygame documentation will be super useful throughout this project.
    Initialize pygame at the beginning of your main() function (take a look at the docs for the syntax).
    Ensure our predefined constants (constants.py) SCREEN_WIDTH and SCREEN_HEIGHT are imported at the top of your file:

from constants import *

Because this is a smaller project, and we don't risk conflicting import names, we're going to use a wildcard import for convenience. In a larger project, you'd want to import only the constants you need.

    Use pygame's display.set_mode() to get a new GUI window:

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Create the game loop. For now, we'll only worry about step 3: drawing the game onto the screen.

    Use an infinite while loop for the game loop. At each iteration, it should:
        Use the screen's fill method to fill the screen with a solid "black" color.
        Use pygame's display.flip() method to refresh the screen. Be sure to call this last!

    It's a good idea to run and test your game frequently as you write code , to make sure it's working as expected:
        If you're on a mac, wait until step 8 before doing this.

python3 main.py

You should see a black window open and stay open.

    Close the game and kill the program with Ctrl+C in the terminal.
    Add the following code to the beginning of each iteration of the game loop:

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.

    Create a .gitignore file and add the following:

venv/
__pycache__/

These files can be regenerated, so they don't need to be tracked.

    Make a git commit! It's a good idea to commit your progress whenever you get something new working.

With the window painting black and closing properly, you're ready to move on to the next step!
