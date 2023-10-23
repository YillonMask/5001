"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def count_down():
    # this function count down from 100 to 1 and print blast
    for i in range(100, 0, -1):
        print(i)
    print("Blastoff!")


def main():
    count_down()


if __name__ == '__main__':
    main()

