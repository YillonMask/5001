"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""
from math import sqrt


def area_triangle(a, b, c):
    # this function calculate the area of triangle of given each side length
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():
    a = float(input('side length of the triangle: '))
    b = float(input('side length of the triangle: '))
    c = float(input('side length of the triangle: '))
    print('the area of the triangle is:', area_triangle(a, b, c))


if __name__ == '__main__':
    main()
