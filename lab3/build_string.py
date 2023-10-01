"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi
"""


def build_string(x, a, b, c):
    # this function takes a string value and three integer values and
    # returns a single string containing 3 lines.
    return a * x + "\n" + b * x + "\n" + c * x


def main():
    x = str(input('Input string:'))
    a = int(input('First integer:'))
    b = int(input('Second integer:'))
    c = int(input('Third integer:'))
    print(build_string(x, a, b, c))


if __name__ == '__main__':
    main()
