Pygame

Now that we have pygame installed, let's write just a bit of boilerplate code so that we have a runnable program to build on.
Assignment

    Create a new file called main.py.
    On the first line, import pygame:

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

    Write a main function that simply prints "Starting Asteroids!" (use this exact text).
    Add this if statement to the end of the file:

if __name__ == "__main__":
    main()

This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. Technically, the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.

    Run the program with python3 main.py

Run and submit the CLI tests using the Boot.dev CLI.
