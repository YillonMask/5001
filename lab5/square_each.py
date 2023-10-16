"""
    CS5001_5003 Fall 2023 SV
    Lab05
    Xinrui Yi
"""


def main():
    pass


def square_each(my_list):
    # this function receives a list as a parameter and return
    # the same list that all the elements are squared
    for i in range(len(my_list)):
        my_list[i] = my_list[i] * my_list[i]
    return my_list


if __name__ == '__main__':
    main()
