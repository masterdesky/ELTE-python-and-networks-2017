import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
PLEASE READ DESCRIPTION!!!!!

The program animates Conway's Game of Life in a borderless arena. The starting structure (life)
could be random or user-defined, as desired. Every life is in the form of a matrix. The matrix
elements should be binary zeros and ones. Ones indicate living cells, zeros indicate dead cells obviously.


RULES OF CONWAY'S GAME OF LIFE:

#1  Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
#2  Any live cell with two or three live neighbours lives on to the next generation.
#3  Any live cell with more than three live neighbours dies, as if by overpopulation.
#4  Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

It means, that:
(from Rosetta Code)
     C   Neighbours        new C
#1   1   0,1             ->  0  # Underpopulation
#2   1   2,3             ->  1  # Lives to the next generation
#3   1   4,5,6,7,8       ->  0  # Overpopulation
#4   0   3               ->  1  # Reproduction


GAME MODES:
# 1. RANDOM: TYPE 'random' AT INITIALIZATION, FOR A GAME WITH A RANDOMIZED LIFE
# 2. USER: TYPE 'user' AT INITIALIZATION FOR A GAME WITH A USER-DEFINED MATRIX (LIFE), WHICH
COULD BE CHANGED AS DESIRED IN THE CODE AT ROW 141. IN THIS MODE READING A MATRIX FROM A FILE
ALSO AVAILABLE
'''

# =========== INITIALIZATION ===========

# WAITS FOR INPUT FROM STDIN
Mode = input("Please choose game mode (random/user): ")

# =========== DECLARATION FOR FIGURE ===========

# SET A FIGURE
GameArena = plt.figure()

# =========== FUNCTIONS ===========
# COUNT NEIGHBOURS OF A CELL
def LifeStep(StartingPoints):
    # X MARKS THE X COORDINATE, Y THE Y COORDINATE
    # THE FUNCTION ROLLS THROUGH EVERY CELL IN THE ARENA. FOR EVERY CELL IT CHECKS
    # FOR ITS NEIGHBOURS (FOR X IN (-1, 0, 1) ETC.), EVERY CELL HAS 8 NEIGHBOURS.
    # THEN THE FUNCTIONS SUMMARIZE ALL THE LIVING CELLS IN THE NEIGHBOURHOOD OF THE CELL.
    # IF THIS SUM IS 3, THEN THE FUNCTION RETURNS. IF THIS SUM IS 2, BUT THE CELL WAS
    # LIVING IN THE PREVIOUS STEP, THE FUNCTION ALSO RETURNS. (THIS IS THE #2 AND #4 RULE)
    Neighbours = sum(np.roll(np.roll(StartingPoints, x, 0), y, 1) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x != 0 or y != 0))
    # SHOULD USE & AND |, BECAUSE IT'S A LOGICAL EXPRESSION??? AND/OR DIDN'T WORK
    return (StartingPoints & (Neighbours == 2)) | (Neighbours == 3)

def AnimateLife(StartingPoints):
    # INPUT DATA SHOULD BE AN ARRAY, SO WE CONVERT INTO IT FROM A LIST
    StartingPoints = np.asarray(StartingPoints)

    # CREATE A FULL NULL-MATRIX IN THE SIZE OF THE FULL ARRAY
    Background = np.zeros_like(StartingPoints)

    # SET ARENA AXES (FROM MATPLOTLIB.ORG)
    ax = GameArena.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)

    # FROM STACKOVERFLOW, PLOTTING BINARY MATRIX WITH WHITE AND BLACK SQUARES
    # ON STACKOVERFLOW IT WAS AN EXAMPLE FOR ANIMATING A FRACTAL
    Image = ax.imshow(StartingPoints, cmap='Greys', interpolation='nearest')

    # WE SHOULD INITIALIZE THE PLOTTING ANIMATION WITH A BACKGROUND FIRST IN MATPLOTLIB'S FuncAnimation
    # THIS IS NECESSARY, BECAUSE THE ANIMATION WOULD ONLY SHOW ONLY ONE FRAME, AND WE DON'T WANT IT
    # THIS IS FROM THE EXAMPLE CODES FROM MATPLOTLIB'S OFFICIAL PAGE
    def InitFunc():
        Image.set_data(Background)
        return Image,

    # STEPPING THE LIFE AND UPDATING THE IMAGE
    def GenerationUpdate(x):
        Image.set_data(GenerationUpdate.StartingPoints)
        GenerationUpdate.StartingPoints = LifeStep(GenerationUpdate.StartingPoints)
        return Image,

    # SET UP FORMATTING FOR MOVIE FILES FROM MATPLOTLIB'T HOME PAGE
    # FFMPEG NEEDED!!!
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='PB'), bitrate=1800)

    # ANIMATE THE OBJECT
    GenerationUpdate.StartingPoints = StartingPoints
    anim = animation.FuncAnimation(GameArena, GenerationUpdate, 400, interval=50, init_func=InitFunc, blit=True)
    anim.save('gameoflifelast.mp4', writer=writer)
    plt.show()


# =========== M-A-I-N ===========


# USER MODE GIVES A USER-DEFINED BINARY MATRIX TO THE PROGRAM, WHICH FUNCTIONS
# AS A DEFINITION FOR THE ANIMATED LIFE. ONES IT THE MATRIX MARKS A LIVING CELL
# ZEROS IN THE MATRIX MARKS A DEAD CELL
if (Mode == "user"):

    print("Game mode is now set to 'user'")
    print("\n")

    SizeOfArena = input("Please enter the length of the arena's sides (suggested size: min. 20): ")
    print("\n")

    # SizeOfArena DEFINES THE DIMENSIONS OF THE PLAYING FIELD
    SizeOfArena = int(SizeOfArena)

    # CREATES THE ARENA FOR THE GAME WITH FULL OF ZEROS
    StartingPoints = np.zeros((SizeOfArena,SizeOfArena), dtype = bool)

    Structure = input("Which structure should we use?:\n"
                  "[a]: Glider(X:3 Y:3)\n"
                  "[b]: Lightweight Spaceship(X:5 Y:4)\n"
                  "[c]: Unbounded Growth(X:5 Y:5)\n"
                  "[d]: Gosper Glider Gun(X:36 Y:9)\n"
                  "[e]: User-defined(X:? Y:?)\n"
                  "[f]: Defined from file(X:? Y:?)\n")

    # GLIDER
    a =[[1,0,0],
        [0,1,1],
        [1,1,0]]

    # LWSP
    b =[[0,0,1,1,0],
        [1,1,0,1,1],
        [1,1,1,1,0],
        [0,1,1,0,0]]

    # UNBOUNDED GROWTH
    c =[[1,1,1,0,1],
        [1,0,0,0,0],
        [0,0,0,1,1],
        [0,1,1,0,1],
        [1,0,1,0,1]]

    # GLIDER GUN
    d =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    # THIS IS WHAT COULD BE MODIFIED
    e = [[1,0,1,0],
         [1,1,1,1],
         [0,1,1,0],
         [0,0,0,1]]

    # SIZE OF THE USER-DEFINED LIFE
    xCoordinate = input("Enter the size of the user-defined life along the X axis: ")
    yCoordinate = input("Enter the size of the user-defined life along the Y axis: ")
    print("\n")


    xCoordinate = int(xCoordinate)
    yCoordinate = int(yCoordinate)

    # DISTANCE OF THE STARTING LIFE FROM THE UPPER LEFT CORNER
    Position = math.ceil(SizeOfArena/5)

    if (((Position+yCoordinate) | (Position+xCoordinate)) > SizeOfArena):
        SizeOfArena = input("Size of arena is too small for this life! It should be at least\n"
                            "[bigger coordinate]+[size of arena/4]. Example: For a life with\n "
                            "the size of 10x5, you need at least an arena with the size of\n"
                            "16x16 cells. Considering this, please enter a bigger arena size: ")
        SizeOfArena = int(SizeOfArena)


    # READ IN STARTING STRUCTURE FROM FORMATTED INPUT
    if(Structure == 'a'):
        StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = a

    elif(Structure == 'b'):
        StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = b

    elif(Structure == 'c'):
        StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = c

    elif(Structure == 'd'):
        StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = d

    elif(Structure == 'e'):
        StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = e

    elif(Structure == 'f'):
        FileName = input("Please enter the file's name, which contains the matrix: ")
        FileReadIn = np.loadtxt(FileName, dtype='i', delimiter=',')
        StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = FileReadIn

    else:
        exit("Please choose a valid structure! The program exits.")

    # ANIMATE THE STEPS
    AnimateLife(StartingPoints)

# RANDOM MODE GENERATES A RANDOM BINARY MATRIX, LESSER THAN A SIZE OF THE ARENA
# THE BEST ARENA SIZE FOR RANDOM LIFE IS GREATER THAN 20 X 20 CELL
elif (Mode == "random"):
    print("Game mode is now set to 'random'")
    print("\n")

    SizeOfArena = input("Please enter the length of the arena's sides (suggested size: min. 20): ")
    print("\n")

    # SizeOfArena DEFINES THE DIMENSIONS OF THE PLAYING FIELD
    SizeOfArena = int(SizeOfArena)

    # GENERATE RANDOM CODE
    np.random.seed(10011)
    StartingPoints = np.zeros((SizeOfArena,SizeOfArena), dtype = bool)

    # SIZE OF THE RANDOMIZED LIFE
    xCoordinate = input("Enter the size of the random life along the X axis: ")
    yCoordinate = input("Enter the size of the random life along the Y axis: ")

    yCoordinate = int(yCoordinate)
    xCoordinate = int(xCoordinate)

    # DISTANCE OF THE STARTING LIFE FROM THE UPPER LEFT CORNER
    Position = math.ceil(SizeOfArena/5)

    if (((Position+yCoordinate) | (Position+xCoordinate)) > SizeOfArena):
        SizeOfArena = input("Size of arena is too small for this life! (it should be at least\n"
                            "[bigger coordinate]+[size of arena/4]. Example: For a life with\n "
                            "the size of 10x5, you need at least an arena with the size of\n"
                            "16x16 cells. Considering this, please enter a bigger arena size: ")
        SizeOfArena = int(SizeOfArena)

    # PUT LIFE INTO THE PLAYING FIELD
    RandomPoints = np.random.random((yCoordinate, xCoordinate))

    StartingPoints[Position:(Position+yCoordinate),Position:(Position+xCoordinate)] = RandomPoints > np.random.random()

    # ANIMATE THE STEPS
    AnimateLife(StartingPoints)

else:
    exit("Arguments should be 'random', or 'user'! The program exits.")
