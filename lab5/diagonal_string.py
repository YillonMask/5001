"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def diagonal_string(word):
    # this function takes a string and returns each letter diagonally
    result = ""
    for i, char in enumerate(word):
        result += " " * i + char
        if i != len(word) - 1:
            result += '\n'
    return result


def main():
    pass


if __name__ == '__main__':
    main()
