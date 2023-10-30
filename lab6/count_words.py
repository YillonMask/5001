"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def name():
    pass


def main():
    """
        this function reads in a sentence and prints each word on its own line
    """
    my_string = input("Enter a sentence: ")
    my_list = my_string.split()
    n = 0
    for word in my_list:
        print(n, ".", ' ', word, sep='')
        n += 1


if __name__ == '__main__':
    main()
