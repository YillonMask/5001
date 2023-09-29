"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""


def plus(x, y):
    # adds together two values and returns the total
    total = x + y
    return total


def main():
    x = float(input("First number to add: "))
    y = float(input("Second number to add: "))
    plus(x, y)
    print('the total of two numbers:', plus(x, y))


if __name__ == '__main__':
    main()
