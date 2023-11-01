"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def find_max(numbers):
    """
        this function takes in a list of integers and returns the
        maximum value from that list using recursive algorithm
    """
    n = len(numbers)
    return find_max_index(numbers, n)


def find_max_index(numbers, n):
    if n == 0:
        return max(numbers)
    else:
        return find_max_index(numbers, n - 1)


def main():
    pass


if __name__ == '__main__':
    main()
