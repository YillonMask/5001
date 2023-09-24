"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    number = int(input('Enter number:'))
    last_digit = number % 10
    first_digit = number // 1000
    print("The first number is", first_digit)
    print("The last number is ", last_digit)


if __name__ == '__main__':
    main()
