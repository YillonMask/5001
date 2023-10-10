"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def extract_letter(word,n):
    # this function returns the correct letter in a word
    my_string=word
    print(my_string[n])


def main():
    word = input('Enter a word: ')
    n = int(input('Enter the index of the letter: '))
    extract_letter(word, n)


if __name__ == '__main__':
    main()
