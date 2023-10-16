"""
    CS5001_5003 Fall 2023 SV
    Lab05
    Xinrui Yi
"""


def main():
    # this function
    result = read_value()
    return result


def read_value():
    values = list()
    while True:
        num = int(input("Enter a number: "))
        if num <= 0:
            break
        values.append(int(num))
    print(values)


if __name__ == '__main__':
    main()
