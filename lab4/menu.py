"""
    CS5001_5003 Fall 2023 SV
    Lab04
    Xinrui Yi
"""


def menu():
    print('0 -- Quit\n'
          '1 -- Add "O"\n'
          '2 -- Add "oo"\n'
          '3 -- Add "xXx"')


def main():
    options = ["O", "oo", "xXx"]
    selected_options = []
    while True:
        menu()
        choice = input("Option: ")
        if choice == '0':
            break
        elif choice in ['1', '2', '3']:
            option_index = int(choice) - 1
            selected_options.append(options[option_index])
        else:
            print('Invalid option')
    results = ''.join(selected_options)
    print('Result:', results)


if __name__ == '__main__':
    main()
