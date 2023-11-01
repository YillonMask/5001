"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def sum_values(my_list, n):
    """
        this function takes in a list of integers and an index
        of one element in the list and returns the sum of all values
        in the list starting with the element provided index and ending with
        the last element in the list
    """
    if n == 0:
        return sum(my_list)
    else:
        total = sum_values(my_list, n - 1) - my_list[n - 1]
        return total


def main():
    pass


if __name__ == '__main__':
    main()
