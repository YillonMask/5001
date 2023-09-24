"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    num = int(input("Enter value: "))
    if num < 0 and num % 2 == 0:
        print("even negative number")
    if num >= 0 and num % 2 == 0:
        print("even positive number")
    if num < 0 and num % 2 != 0:
        print("odd negative number")
    if num > 0 and num % 2 != 0:
        print("odd positive number")


if __name__ == '__main__':
    main()
