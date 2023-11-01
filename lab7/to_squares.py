"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def to_squares(my_list, n):
    """
        this function takes in a list of integers and an index
        of one element in the list and returns the same list 
        where the elements from the provided index  to the end of the list 
        have been squared.
    """
    if n == 0:
        my_list_squared = [x ** 2 for x in my_list]
        return my_list_squared
    else:
        my_list_squared = to_squares(my_list, n - 1)
        my_list_squared[n - 1] = my_list[n - 1]
        return my_list_squared


def main():
    print(to_squares([5], 0))


if __name__ == '__main__':
    main()
