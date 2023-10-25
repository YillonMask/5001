"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def count_negatives(my_list):
    """
        this function count how many negative integers in a given list
    """
    n = len(my_list)
    count = 0
    for num in my_list:
        if num < 0:
            count += 1
    return count


def main():
    pass


if __name__ == '__main__':
    main()
