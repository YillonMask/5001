"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def add_ten(num):    
    """
        this function recieves a list of integer and add ten to each element
    """
    n = len(num)
    for i in range(n):
        num[i] = num[i] + 10
    return num


def main():
    pass


if __name__ == '__main__':
    main()
