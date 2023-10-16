"""
    CS5001_5003 Fall 2023 SV
    Lab00
    Xinrui Yi
"""


def name_number(name):
    # this function calculate the name number of a given name
    count = 0
    for char in name:
        index = ord(char) - ord('a') + 1
        count += index
    return count


def main():
    pass


if __name__ == '__main__':
    main()
