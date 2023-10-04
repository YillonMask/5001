"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def menu():
    print('0 -- Quit\n'
          '1 -- Add "0"\n'
          '2 -- Add "oo"\n'
          '3 -- Add "xXx"' )
    choice = input("Option: ")
    return choice


def main():
    while True:
        option = menu()
        if option == '0':
            break
    print('thx',option)


if __name__ == '__main__':
    main()
