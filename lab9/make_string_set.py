"""
    CS5001_5003 Fall 2023 SV
    Lab09
    Xinrui Yi
"""


def make_string_set(my_string):
    """
        this function take string into set
    """
    items = my_string.split(',')
    items = [item for item in items if item != ' ' and item != '']
    string_set = set(strings.strip() for strings in items)
    return string_set


def main():
    my_string = ''
    make_string_set(my_string)


if __name__ == '__main__':
    main()
