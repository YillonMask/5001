"""
    CS5001_5003 Fall 2023 SV
    Lab11b Dice Class
    Xinrui Yi
"""
import random


class Dice:
    """ Class: Dice
        Attributes: sides, color, value
        Methods: roll(), get_color(), get_value(), __str__
    """

    def __init__(self, sides, colors="white"):
        """
        Constructor -- creates new instances of Dice
        Parameters:
           self -- the current object
           colors: A string naming a color such as "red" or "blue"
           (optional  for the constructor, defaults to "white")
        """
        if sides < 6:
            raise ValueError("There should be at least 6 sides")
        if not isinstance(sides, int):
            raise TypeError("The sides should be an integer")
        self.sides = sides
        self.colors = colors
        self.value = random.randint(1, sides)

    def roll(self):
        """
            Method -- roll the dice by choosing a new random sides
                      returns the value
            Parameters:
               self -- the current object
        """
        print(f'before the roll, the initial value of the dice is {self.value}')
        self.value = random.randint(1, self.sides)
        print(f'After one roll, the current value is {self.value}')

    def get_color(self):
        """
        Method -- returns the color of the die
        Parameters:
            self -- the current object
        """
        return self.colors

    def get_value(self):
        """
        Method -- return the current value
        Parameters:
            self -- the current object
        """
        return self.value

    def set_color(self, new_color):
        """
        Method -- set the dice to new color
        Parameters:
            self -- the current object
            new_color -- color wants to set to
        """
        self.colors = new_color
        print(f'The color of dice is set to {self.colors}')

    def __str__(self):
        print(f"The dice is in color {self.colors}, the current value is {self.value}.")


def main():
    die1 = Dice(6, colors='white')
    die1.roll()
    die1.get_value()
    die1.__str__()
    die2 = Dice(5, colors='white')


if __name__ == '__main__':
    main()
