"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""


def first(x, y):
    # receives two parameters and return smaller one
    if x < y:
        return x
    else:
        return y


def main():
    x = input("First value: ")
    y = input("Second value: ")
    print('the smaller one between these two:', first(x, y))


if __name__ == '__main__':
    main()
