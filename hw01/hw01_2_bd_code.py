"""
    CS5001_5003 Fall 2023 SV
    HW01P02
    Xinrui Yi
"""


def name(x):
    # this function
    pass

def main():
    current_year = 2023
    user_name = input("Welcome! What is your name?")
    print("Hi, ", user_name, ".", sep='')
    user_age = int(input("How old are you?"))
    user_birth = current_year - user_age
    print("I guess you were born in ", user_birth, ".", sep='')

if __name__ == '__main__':
    main()
