"""
    CS5001_5003 Fall 2023 SV
    Lab10
    Xinrui Yi
"""


class Name:
    """represents a person's full name consisting of a first name
        and a last name.
        Your class should also store a nick name for the person
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        if not isinstance(self.first_name, str):
            raise TypeError('The input is not string')
        if first_name == "":
            raise ValueError('Empty input')
        self.last_name = last_name
        if not isinstance(self.last_name, str):
            raise TypeError('The input is not string')
        if last_name == "":
            raise ValueError('Empty input')
        nick_name = first_name

    def get_first_name(self):
        try:
            return self.first_name
        except TypeError:
            raise TypeError('Invalid input type')

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_nick_name(self, nick_name):
        self.nick_name = nick_name
        if not isinstance(nick_name, str):
            raise TypeError('The input is not string')
        if nick_name == "":
            raise ValueError('Empty input')

    def get_nick_name(self):
        return self.nick_name

    def __str__(self):
        return f'{self.first_name} "{self.nick_name}" {self.last_name}'
