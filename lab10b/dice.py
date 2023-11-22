"""
    CS5001_5003 Fall 2023 SV
    Lab11b Dice Class
    Xinrui Yi
"""
import random


class Dice:
    """Class Dice
        Attributes: sides, color, value
        Methods: roll(), get_color(), get_value(), __str__
    """

    def __int__(self,sides, colors = "white"):
        """
        parameter: sides The number of sides on the die
                (must be an int >= 6, else raise an appropriate Exception)
                 color: A string naming a color such as "red" or "blue"
                 (optional  for the constructor, defaults to "white")
        """
        """
                Constructor -- creates new instances of coffee
                Parameters:
                   self -- the current object
                   coffee_name -- the initial name of this coffee
                   size (optional) -- the initial size of this coffee
        """
        if sides >= 6:
            raise ValueError
        if not isinstance(sides, int):
            raise TypeError
        self.sides = sides
        self.colors = colors


def roll():
    """
        this function
    """



def main():


if __name__ == '__main__':
    main()
