"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    num = int(input("Enter value: "))
    if num >= 1 and num <= 100:
        print(num)
    elif num < 1:
        print("Too small, clamping required")
        print("Value is 1")
    else:
        print("Too big, clamping required")
        print("Value is 100")


if __name__ == '__main__':
    main()
