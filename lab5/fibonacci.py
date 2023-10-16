"""
    CS5001_5003 Fall 2023 SV
    Lab05
    Xinrui Yi
"""


def fibonacci(n):
    # this function receives a single positive integer 
    # and returns a list contains the n Fibonacci numbers
    result = [1] * n
    for i in range(2, n):
        result[i] = result[i - 1] + result[i - 2]
    return result


def main():
    pass


if __name__ == '__main__':
    main()
