"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""


def is_equal(x, y):
    # receives two parameters and return if they are equal
    return x == y


def main():
    x = input("First value: ")
    y = input("Second value: ")
    if is_equal(x, y):
        print('Two values are euqal! :)')
    else:
        print('Two values are not equal :(')


if __name__ == '__main__':
    main()
