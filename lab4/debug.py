"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def name():
    # this function
    pass


def main():
    hi = int(input("Enter larger: "))
    lo = int(input("Enter smaller: "))
    while lo > hi:
        lo = int(input("Enter smaller: "))
    print(hi, lo, sep='')


if __name__ == '__main__':
    main()
