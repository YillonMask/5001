"""
    CS5001, Fall 2023, Silicon Valley, hw03, q1
    Sample Midterm Question, just for practice, to help with preparation.
    The actual Midterm will pose different questions, about similar material.

    Problem: Working with Sentences

    Natural language processing programs often work with 'cleaned up' data,
    such as after removing punctuation and simplifying in other ways. This
    question illustrates some ways that built-in string methods are helpful.
    Notice the top-of-file and top-of-function doc string formats.

    Hints/Reminders:
    - The .strip() method of strings helps with leading/trailing punctuation.
    - The .replace() method of strings may also be helpful.
    - for loops can help iterate over strings, lists, and tuples.
    - The .split() method of strings may also come in handy.
    - Check here for details: https://docs.python.org/3/library/stdtypes.html
    - PUNCTUATION is defined as any char in the following constant string:
"""

PUNCTUATION = ".,!?-:;\t\n()[]{}@#\\$%^*-_+= /'\"|~<>"


def sentences(prompt):
    """ Accepts keyboard input and returns tuple: (list of words, int length).

        :param prompt: str to print to request keyboard input from user
        :return: list of words (strings) in simplified format
        :return: integer length of word list after processing

        One might imagine the main loop of a chatbot calling this.
        The chatbot is meant to exchange remarks with a casual user.
        Since two values are returned, caller may opt to accept in two vars,
        or treat the returned values as a tuple of a list and an integer.

        The list portion of the return should contain only UPPERCASE words.
        There should be no whitespace or punctuation (as defined here).
        Other than the prompt requesting keyboard input, your function should
        not print to the screen. (When called from IDLE, of course,
        the returned tuple will be printed by the read-eval-print loop.)

        A main() function is NOT required, but may be included if helpful to
        you in the course of designing or testing your solution. If you
        include it, be sure to end the file with "if ... __main__ ..." clause.

        Examples of desired input/output behavior follow:

        >>> sentences("Please enter a sentence:\n")
        Please enter a sentence:
        Time flies, like an arrow!!!
        (['TIME', 'FLIES', 'LIKE', 'AN', 'ARROW'], 5)

        >>> sentences("Please enter another sentence:\n")
        Please enter another sentence:
        Odd -- and fruit flies like a banana?
        (['ODD', 'AND', 'FRUIT', 'FLIES', 'LIKE', 'A', 'BANANA'], 7)
    """

    # Your code should replace this comment and the following pass statement
    PUNCTUATION = ".,!?-:;\t\n()[]{}@#\\$%^*-_+= /'\"|~<>"
    my_list = 
    
    for puctuation 
    
    pass
