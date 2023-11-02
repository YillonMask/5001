"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def upper_triangle(n):
    """
        this function takes in number greater
        than or equal to 3
        and prints an upper left triangle of that size
    """
    if n >= 1:
        print('*' * n)
        upper_triangle(n - 1)


def main():
    print(upper_triangle(5))


if __name__ == '__main__':
    main()
