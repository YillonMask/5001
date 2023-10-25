"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def filter_evens(nums):
    """
        this function receives a list of integer and return
        new list that only even elements of the list
    """
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result


def main():
    pass


if __name__ == '__main__':
    main()
