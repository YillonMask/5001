"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def choose(k, n):
    """
        this function computes the number of combinations
        possible given k and n where n>=k>=0
    """
    if k == 1 or k == n - 1:
        return n
    elif n == k or k == 0:
        return 1
    else:
        return choose(k - 1, n - 1) + choose(k, n - 1)


def main():
    print(choose(2, 6))


if __name__ == '__main__':
    main()
