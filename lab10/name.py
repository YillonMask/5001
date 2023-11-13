"""
    CS5001_5003 Fall 2023 SV
    Lab10
    Xinrui Yi
"""


class Name:
    """represents a person's full name consisting of a first name and a last name. 
        Your class should also store a nick name for the person
    """


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        nick_name = first_name


    def get_first_name(self):
        return self.first_name


    def get_last_name(self):
        return self.last_name


    def get_full_name(self,last_name, first_name):
        return self.last_name + self.first_name


    def set_nick_name(self, nick_name):
        self.nick_name = nick_name


    def get_nick_name(self):
        return self.nick_name
