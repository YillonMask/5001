"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def diagonal_string(word):
    # this function takes a string and returns each letter diagonally
    index = 0
    while index < len(word):
        space = index * ' '
        print(space + word[index])
        index = index + 1
        space = index


def main():
    pass


if __name__ == '__main__':
    main()
