"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""
PI = 3.14159 


def volume_sphere(r):
    # this function calculate the volume of the sphere of given radius
    volume = (4 / 3) * PI * r**3
    return volume


def main():
    r = float(input('the radius of sphere: '))
    print('the volume of the sphere is:', volume_sphere(r))


if __name__ == '__main__':
    main()
