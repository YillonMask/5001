"""
    CS5001_5003 Fall 2023 SV
    HW02P3
    Xinrui Yi
"""


def is_leap_year(year):
    # this function accepts a year and return True if it is a leap year
    # or False it is not
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    done = False
    n = 0
    while not done:
        x = int(input('Please enter a year greater than 0: '))
        if is_leap_year(x):
            print('The year', x, 'is a leap year')
        else:
            print('The year', x, 'is not a leap year')
        n = n + 1
        if n == 12:
            done = True


if __name__ == '__main__':
    main()
