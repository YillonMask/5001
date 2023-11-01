"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def factorial(n):
    """
        this function takes in positive number and returns its factorial
        using recursive way
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print(factorial(4))


if __name__ == '__main__':
    main()
