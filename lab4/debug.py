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
    while hi >= lo:
        print(hi)
        hi = hi - 1    


if __name__ == '__main__':
    main()
