"""
    CS5001_5003 Fall 2023 SV
    Lab08
    Xinrui Yi
"""


def name():
    """
        this function
    """
    pass


def main():
    value1 = int(input("Enter value: "))
    while value1 == 0:
        print("Value should be either negative or positive")
        value1 = int(input("Enter value: "))
    value2 = int(input("Enter value: "))
    while value1 * value2 >= 0:
        if value1 > 0:
            print("Value should be negative")
            value2 = int(input("Enter value: "))
        else:
            print("Value should be positive")
            value2 = int(input("Enter value: "))
    if value1 >= value2:
        print("Pair:", (value2, value1))
    else:
        print("Pair:", (value1, value2))


if __name__ == '__main__':
    main()
