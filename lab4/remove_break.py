"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def name():
    # this function
    pass


def main():
    a = 0
    b = 1
    print('0\n1')
    done = False
    while not done:
        c = a + b
        print(c)
        a = b
        b = c
        if c > 1000:
            done = True


if __name__ == '__main__':
    main()
