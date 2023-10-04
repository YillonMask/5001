"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def multiples():
    # this function asks for non-zero integer
    # and prompts the user to enter multiples
    # asks user to Try again until a multiple is entered
    non_zero_integer = int(input('Enter a non-zero integer: '))
    multiples = int(input('Enter multiple: '))
    while multiples % non_zero_integer != 0:
        multiples = int(input('Try again: '))


def main():
    multiples()


if __name__ == '__main__':
    main()
