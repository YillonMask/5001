"""
    CS5001_5003 Fall 2023 San Jose
    Midterm Exam
    Question 2. Debugging Strange Circles

    A. The following 2 functions may have some bugs. Read them carefully!
       Create 3 tests and run them on both of the 2 functions.
       Implement your tests by running your test code from main().
       Avoid repetitive code (eg break into smaller functions as needed).
       Keep track of tests failed, and print your final results.
       Some code has been provided to help you get started with the testing.

    B. Run your tests once. First, just fix any bugs in your testing code.
       Now capture a transcript of running the tests on the provided functions,
       before fixing them.
       You can do this in IDLE, using "Save As" to a .txt file. (You may use
       another IDE iff you know how to save a transcript to a .txt file.)

       Be careful. Sometimes a bug in 1 function can cause problems in another.

    C. Then, fix any bugs in the 2 provided functions.
       Finally, repeat Step B, using the corrected functions.

    Turn in your updated circles.py file plus both testing transcripts. The
    second transcript should reflect any additional debugging you had to do.
"""

import math
PI = math.pi
EPSILON = 0.000001


def area(radius):
    """ Given a radius (float or int), returns the area of a circle """
    return PI * radius ** 2


def indiana_area(radius):
    """ For a good laugh -- Google for PI, Indiana, StraightDope!
        Here, you must assume that Indiana was right about PI!
        Be careful though -- what is this function supposed to do?
    """
    global PI
    PI = 3.0
    return PI * radius ** 2


def test_area(radius, expected):
    """ Returns True if returned area matches expected area, else False
        Here is a head start to illustrate how testing is done.
    """
    return abs(area(radius) - expected) < EPSILON


def test_indiana_area(radius, expected):
    # Now it is your turn
    return abs(indiana_area(radius) - expected) < EPSILON


def main():
    """ Main should run 3 tests each for the 2 functions.
        It should keep track of fails and print a summary line.
        Your solution should use a for loop.
        Use a list of tuples [(test_data, expected), ...] for
        each of the 3 functions. One example is provided, so just 2 to go!
        Avoid repetitive code!
    """
    # The next 2 lines of code need a 3rd tuple of (radius, expected).
    area_tests = [(0, 0.0), (1, 3.141592653589793), (2, 12.566370614359172)]
    indiana_area_tests = [(0, 0.0), (1, 3.0), (2, 12.0)]

    # Run the list of test cases for the area function:
    failed = 0
    for test_pair in area_tests:
        if not test_area(test_pair[0], test_pair[1]):
            failed += 1
    print("The area function failed", failed, "tests.")

    failed = 0
    # Now run the list of test cases for the indiana_area function:
    for test_pair in indiana_area_tests:
        if not test_indiana_area(test_pair[0], test_pair[1]):
            failed += 1
    print("The indianna area function failed", failed, "tests.")


if __name__ == '__main__':
    main()
