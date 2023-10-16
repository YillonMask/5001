"""
    CS5001_5003 Fall 2023 SV
    Lab00
    Xinrui Yi
"""


def main():
    # this function
    result = read_value()
    print(result)


def read_value():
    values = []
    while True:
        num = int(input("Enter a number: "))
        if num <= 0:
            break
        values.append(int(num))
    return values


if __name__ == '__main__':
    main()
