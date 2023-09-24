"""
    CS5001_5003 Fall 2023 SV
    Lab00
    Shiqiu Chen / Xinrui Yi
"""


"""
    def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    diagnal = (width ** 2 + height ** 2) ** 0.5
    print("The area of recatangle is : " + str(area))
    print("The perimeter of recatangle is : " + str(perimeter))
    print("The diagnal of recatangle is : " + str(diagnal))

"""


def main():
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    area = width * height
    perimeter = 2 * (width + height)
    diagonal = (width ** 2 + height ** 2) ** 0.5
    print("The area of the rectangle is", area)
    print("The perimeter of the rectangle is", perimeter)
    print("The diagonal of the rectangle is", diagonal)


if __name__ == '__main__':
    main()
