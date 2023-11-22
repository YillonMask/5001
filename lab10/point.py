"""
    CS5001_5003 Fall 2023 SV
    Lab10
    Xinrui Yi
"""
import math


class Point:
    """
        Write a class called Point
        that represents a point in three-dimensional space.
        A point stores its x, y, and z coordinate as integral values.
        Your class should implement the following methods:
        get_distance(origin=None).
        that receives another point as a parameter and
        calculates the distance to the parameter point.
        If a point is not provided, it should calculate the distance
        from the current point to the origin.
    """

    def __init__(self, x, y, z):
        if not all(isinstance(i, int) for i in [x, y, z]):
            raise TypeError('Coordinates must be numeric')
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_distance(self, origin=None):
        if origin is None:
            origin = Point(0, 0, 0)
        elif not isinstance(origin, Point):
            raise TypeError
        distance = math.sqrt((self.x - origin.x) ** 2 +
                             (self.y - origin.y) ** 2 +
                             (self.z - origin.z) ** 2)
        return distance

    def __str__(self, origin=None):
        return f'Point: ({int(self.x)}, {int(self.y)}, {int(self.z)})'
