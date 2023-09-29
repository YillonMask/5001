"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui
"""


def line():
    # this function returns a string that consists of 50 copies of the x letter
    res = 50 * 'x'
    return res


def main():
    line()
    print('50 copies of x:', line())


if __name__ == '__main__':
    main()
