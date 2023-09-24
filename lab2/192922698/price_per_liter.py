"""
    CS5001_5003 Fall 2023 SV
    Lab02
    Xinrui Yi / Shiqiu Chen
"""


def calculator(price1, price2):
    price1_per_liter = price1 / 6 / 0.355
    price2_per_liter = price2 / 2
    print("Six-pack price per liter: " + str(price1_per_liter))
    print("Two-liter price per liter: " + str(price2_per_liter))


def main():
    price1 = float(input("Price per six-pack: "))
    price2 = float(input("Price per two-liter: "))
    calculator(price1, price2)


if __name__ == '__main__':
    main()
