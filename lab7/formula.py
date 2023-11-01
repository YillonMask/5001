"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def formula(x):
    """
        this function returns the result of given mathematical formula
        using recursive way
    """
    if x <= 1:
        return 3
    else:
        result = 2 * formula(x - 1) + 5
        return result


def main():
    x = int(input("Enter a number"))
    print(formula(x))


if __name__ == '__main__':
    main()
