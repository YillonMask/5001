"""
    CS5001_5003 Fall 2023 SV
    HW02
    Xinrui Yi
"""


def name():
    # this function
    pass

def main():
    # Bug 1: ZeroDivisionError (Python-specific)
    # This bug occurs when dividing a number by zero.

    result = 10 / 0  # Causes ZeroDivisionError

    
    # Bug 2: SyntaxError due to unclosed parentheses (General type) 
    # This bug occurs when parentheses are not closed properly.

    result = (10 + 5 * 2  # Missing closing parenthesis
    print(result)

    # Bug 3: Indentation Error (Python-specific)
    # This bug occurs when a block of code is not properly indented.

    if True:
    print("This line is not indented correctly and will cause an IndentationError.")    
    
    # Bug 4: undefined variable (General)
    # This bug occurs when using an undefined variable or function.

    x = 5
    y = x + z  # Causes undefined variable 'z'


if __name__ == '__main__':
    main()
