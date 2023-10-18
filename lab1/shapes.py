"""
    CS5001 Fall 2023
    Turtle Square Example
    Xinrui Yi
"""

from turtle import *


def equitri(length):
    forward(length)
    right(120)
    forward(length)
    right(120)
    forward(length)
    right(120)


def square(length):
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)


def main():
    how_big = int(input("How big are the sides you want? "))
    square(how_big)
    equitri(how_big)
    print("Done!")
    exitonclick() #need to exit turtle!


if __name__ == '__main__':
    main()
