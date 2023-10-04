"""
    CS5001_5003 Fall 2023 SV
    Lab00
    Xinrui Yi
"""


def print_evens():
    # this function prints the even numbers from 2 to 100
    num = 1
    while num <= 50:
        print(2 * num)
        num = num + 1


def main():
    print_evens()


if __name__ == '__main__':
    main()
