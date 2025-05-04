Modules

It would be a massive pain if we had to fit all of our code into a single file.
Importing

In Python, each .py file is a module, and we can import functions, variables, and classes from one module into another with the import statement. The name of a module is the filename (without the .py extension).

# import the connect_database function
# and the database_version variable
# from database.py into the current file
from database import connect_database, database_version

If you want to import everything from a module, you can use the * character:

# import everything from the module
# database.py into the current file
from database import *

However, it's generally recommended to avoid wildcard imports (*) as they make your code harder to read and debug. You can read more about this in the Python style guide.
Constants

Games often have a lot of magic numbers to represent things like player speeds, item costs, and attack damage. We will use this file as a place to store those kind of constant values.
Assignment

    Create a new file in your project called constants.py (in the same folder as main.py), and paste this in:

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

    Import everything from the constants.py file into main.py
    Print out the SCREEN_WIDTH and SCREEN_HEIGHT values when main.py is run. Use the following format:

Along with a greeting from importing pygame, the expected output is the following:

Starting Asteroids!
Screen width: 1280
Screen height: 720

Run and submit the CLI tests.
