"""
    CS5001, Fall 2023, Silicon Valley, hw03, q2
    Sample Midterm Question, just for practice, to help with preparation.
    The actual Midterm will pose different questions, about similar material.

    Uses the Python turtle to draw shapes
    Emphasis: validating user input, while loops.
    Mark Miller, starter code, student to complete.
    More about turtle here:
        https://docs.python.org/3/library/turtle.html

    Write a program that accepts user input to determine: how many sides for an
    equilateral polygon, x and y coordinates to start the polygon; the initial
    heading of the turtle (0 degrees means 'right', 90 degrees means 'up',
    180 or -180 means 'to the left', and -90 means 'down'); the size of the
    polygon's sides, and the color of the polygon. Be sure to check validity
    of every user input. The program should include an outer 'while True' loop
    to enable the user to keep adding additional polygons, stopping only when
    the number of sides requested is 0. Do not use a 'break' statement.
    If user specifies 'random' for the color argument, choose randomly from the
    list of colors (this should be handled by the main()).

    (The Midterm will expect good function doc strings. Use the doc string
    for poly shown here as a model.)
"""

from turtle import *  # Load all the methods of the turtle library
from random import choice

COLORS = ['black', 'white', 'red', 'green', 'blue', 'yellow', 'orange']

MAX_X = 400  # Assumes 800x800 window with (0, 0) at the middle of the screen
MAX_Y = 400
MIN_X = -400
MIN_Y = -400


def poly(sides, start_x, start_y, start_hdg, size, color):
    """ Draws polygon with specified sides, position, heading, size, and color.

        Assumes that arguments provided were already validated by caller.

        Parameters:
            sides : int
                    positive int for the number of sides
            start_x : float or int
                      starting position x coordinate
            start_y : float or int
                      starting position y coordinate
            start_hdg : float or int
                        initial heading of turtle
            size : float or int
                   length of each side
            color : string
                    string specifying a legal color (must be in COLORS)
                    

        Returns:
            list : A list of the arguments provided by the caller
    """

    # Invisibly set up the starting position
    penup()
    setx(start_x)
    sety(start_y)
    setheading(start_hdg)
    pencolor(color)
    fillcolor(color)
    pendown()

    # Draw the polygon, with filling enabled
    begin_fill()
    for side in range(sides):
        forward(size)
        right(360/sides)
    end_fill()
    exitonclick() 
    print("A list of arguments provided by the caller:","\n",
          [sides, start_x, start_y, start_hdg, size, color])


def main():
    """ Repeatedly prompt user for parameters to draw variety of polygons

        Stop when user specifies 0 as the number of sides.
        Do not use break statements.
        
        Type-checking need not be performed for ints and floats; however,
        value-checking is required (eg to ensure drawings are within bounds).
        For this example, validity checking is main()'s responsibility.

        The color must be a string on the global list COLORS. However, if user
        specifies 'random' for color, then just choose randomly from COLORS.
    """

    done = False
    while not done:
        sides = int(input("How many sides for your polygon (0 to quit): "))
        if sides == 0:
            done = True
        else:
            start_x = float(input("starting position x coordinate: "))
            start_y = float(input("starting position y coordinate: "))
            # make sure the drawings are within bounds
            while (start_x > MAX_X or start_x < MIN_X or start_y > MAX_Y or
            start_y < MIN_Y):
                start_x = float(input("starting position x coordinate: "))
                start_y = float(input("starting position y coordinate: "))
            color = input("Enter a color you want: ")
            if color == "random":
                index = choice(list(range(len(COLORS))))
                color = COLORS[index]
            start_hdg = float(input("Initial heading of turtle: "))
            size = float(input("Length of each side: "))
            return poly(sides, start_x, start_y, start_hdg, size, color)
        


if __name__ == '__main__':
    main()
