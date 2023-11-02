"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def in_english(n):
    """
        this function taks a integer value as input
        and returns a tring containing the digits of the number in English
    """
    if n == 0:
        return ""
    digit_to_word = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                     5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    if n // 10 != 0:
        return in_english(n // 10) + " " + digit_to_word[n % 10]
    else:
        return digit_to_word[n % 10]


def main():
    print(in_english(123))


if __name__ == '__main__':
    main()
