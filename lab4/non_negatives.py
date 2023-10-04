"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def non_negatives(x):
    # this function reads integer from input. When a non-negative value is read
    # it should print the value.Otherwise, it should stop.
    while x >= 0:
        print(x)
        x = int(input('Enter an integer:'))


def main():
    x = int(input('Enter an integer:'))
    non_negatives(x)


if __name__ == '__main__':
    main()
