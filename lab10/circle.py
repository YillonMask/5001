"""
    CS5001_5003 Fall 2023 SV
    Lab10
    Xinrui Yi
"""
import math


class Circle:
    """
        Write a class called Circle that represents a circle. Each circle has a point of reference to
        it's center stored as x and y coordinates along with its radius. Your class should implement the following methods:
        get_area. returns the area of the circle
        get_distance(x, y). returns the distance from parameter values for x and y to the center of the circle
    """


    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


    def get_distance(self, a, b):
        x = self.x 
        y = self.y
        distance = math.sqrt((x - a)** 2 + (y - b)**2)
        return distance

    
    def get_area(self, radius):
        radius = self.radius
        area = math.pi * radius**2
        return area