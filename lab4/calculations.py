"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def calculations(n):
    # this function ask input for number of integer values to read
    # and print the sum and average of input integer
    total_sum = 0
    while n > 0:
        x = int(input('Enter an integer: '))
        total_sum = total_sum + x
        n = n - 1
    return total_sum


def main():
    n = int(input('Enter the number of values to read: '))
    if n > 0:
        total_sum = calculations(n)
        print('The sum is', total_sum)
        print('The average is', total_sum / n)
    else:
        print('The sum is', 0)
        print('The average is', 0)


if __name__ == '__main__':
    main()
