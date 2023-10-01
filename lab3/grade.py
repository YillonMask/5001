"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""


def grade(x):
    # this function receives a score and returns the letter grade accordingly
    if x >= 93 and x <= 100:
        return 'A'
    elif x >= 90 and x < 93:
        return 'A-'
    elif x >= 86 and x < 90:
        return 'B+'
    elif x >= 82 and x < 86:
        return 'B'
    elif x >= 77 and x < 82:
        return 'B-'
    elif x >= 73 and x < 77:
        return 'C+'
    elif x >= 69 and x < 73:
        return 'C'
    elif x >= 65 and x < 69:
        return 'C-'
    else:
        return 'F'


def main():
    x = float(input('Please input your score:'))
    print('Your grade is:', grade(x))


if __name__ == '__main__':
    main()
