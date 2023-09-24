"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    if num1 == num2 and num3 == num4:
        print(num1, num2, num3, num4, "two pairs")
    elif num1 == num3 and num2 == num4:
        print(num1, num2, num3, num4, "two pairs")
    elif num1 == num4 and num2 == num3:
        print(num1, num2, num3, num4, "two pairs")
    else:
        print(num1, num2, num3, num4, "not two pairs")


if __name__ == '__main__':
    main()
