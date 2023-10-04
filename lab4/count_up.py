"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def count_up(x):
    # this function takes a positive integer as a parameter
    # and prints all the number between 1 and that integer
    integer = x
    n = 1
    while n <= x:
        print(n)
        n = n + 1


def main():
    x = int(input('Please input a positive integer:'))
    count_up(x)


if __name__ == '__main__':
    main()
