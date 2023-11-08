"""
    CS5001_5003 Fall 2023 SV
    Lab08
    Xinrui Yi
"""


def validation(a, b):
    """
        this function validate the input and calculate the multiplication of
        two given value
    """
    if not isinstance(a, int):
        raise TypeError("a should be an integer.")
    if a >= 0:
        raise ValueError("a should be negative.")
    if not isinstance(b, float):
        raise TypeError("b shoulde be a float.")
    if b >= 1000 or b <= 0:
        raise ValueError("b should be positive and less than 1000.")
    result = a * b
    return result


def main():
    negative_integer = int(input("Enter a negative integer value: "))
    positive_float = float(input("Enter a positive number less than 1000: "))
    result = validation(negative_integer, positive_float)
    print("The multiplication of two given value is :", result)


if __name__ == '__main__':
    main()
