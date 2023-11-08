"""
    CS5001_5003 Fall 2023 SV
    Lab08
    Xinrui Yi
"""

import random
random.seed(0)


def generate_random_error():
    value = random.randint(0, 3)
    if value == 0:
        # raise ZeroDivisionError(value)
        print(f"Zero division error -- {value}")
    elif value == 1:
        # raise TypeError(value)
        print(f"Type error raised   -- {value}")
    elif value == 2:
        # raise ValueError(value)
        print(f"Value error raised  -- {value}")
    else:
        # raise NameError(value)
        print(f"Name error raised   -- {value}")


def main():
    done = False
    count = 0
    while count < 20:
        generate_random_error()
        count += 1 


if __name__ == '__main__':
    main()
