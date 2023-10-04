"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def read_words():
    # this function prompts user to input words and read in from keyboard
    # until 'stop' is entered. After it is done, it prints all words in single line
    x = input('Enter a word: ')
    


def main():
    while True:
        x = read_words()
        if x == 'stop':
            break
    print()


if __name__ == '__main__':
    main()
