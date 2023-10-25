"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def positional_elements(num):    
    """
        this function find the element that its value equals to its index
        and return the total number of the element
    """
    n = len(num)
    count = 0
    for i in range(n):
        if i == num[i]:
            count += 1
    return count


def main():
    pass


if __name__ == '__main__':
    main()
