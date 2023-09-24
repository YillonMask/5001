"""
    CS5001_5003 Fall 2023 SV
    Lab03
    Xinrui Yi 
"""


def main():
    length = float(input('Enter length:'))
    inches = 39.3701 * length
    feet = 3.2808416666 * length
    miles = 0.000621371 * length
    print("The length in inches is", inches)
    print("The length in feet is", feet)
    print("The length in miles is", miles)


if __name__ == '__main__':
    main()
