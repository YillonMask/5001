"""
    CS5001_5003 Fall 2023 SV
    Lab10
    Xinrui Yi
"""


class Point:
    """
        Write a class called Point that represents a point in three-dimensional space. 
        A point stores its x, y, and z coordinate as integral values. Your class should implement the following methods:
        get_distance(origin=None). that receives another point as a parameter and calculates the distance to the parameter point. 
        If a point is not provided, it should calculate the distance from the current point to the origin. Hint: Use optional parameters to solve this
    """


    def __init__(self, x, y, z, origin = (0, 0, 0)):
        self.x = x
        self.y = y
        self.z = z
        self.origin = origin


    def get_distance(self):
        return self.first_name


    def get_last_name(self):
        return self.last_name


    def get_full_name(self,last_name, first_name):
        return self.last_name + self.first_name


    def set_nick_name(self, nick_name):
        self.nick_name = nick_name


    def get_nick_name(self):
        return self.nick_name
