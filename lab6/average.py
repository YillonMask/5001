"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def main():
    # this function
    pass


def calculate_average(my_list):
    """
        this function calculate average of a list of integer values
    """
    n = len(my_list)
    if n == 0:
        return 0
    total_sum = 0
    for num in my_list:
        total_sum += num
    return total_sum / n


if __name__ == '__main__':
    main()
