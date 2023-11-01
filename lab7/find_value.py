"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def find_value(my_strings, target):
    """
        this function takes a list of strings and a target value
        and returns whether the target value is in the list of strings
    """
    n = len(my_strings)
    return find_value_index(my_strings, target, n)


def find_value_index(my_strings, target, n):
    if n == 0:
        return (target in my_strings)
    else:
        return find_value_index(my_strings, target, n - 1)


def main():
    print(find_value("abcde", "f"))


if __name__ == '__main__':
    main()
