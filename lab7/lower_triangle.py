"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def lower_triangle(n):
    current = 1
    return lower_triangle_index(n, current)


def lower_triangle_index(n, current):
    """
        this function takes in a number greater than or equal to 3 
        and prints an lower left triangle of that size.
    """
    if current <= n:
        print('*' * current)
        lower_triangle_index(n, current + 1)    


def main():
    print(lower_triangle(5))


if __name__ == '__main__':
    main()
