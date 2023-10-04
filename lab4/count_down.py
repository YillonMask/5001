"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def count_down(x):
    # this function takes a positive integer as a parameter
    # and prints all the number starting with the integer down to 1
    n = 1
    while x >= 1:
        print(x)
        x = x - 1


def main():
    x = int(input("Please input a positive number:"))
    count_down(x)


if __name__ == '__main__':
    main()
