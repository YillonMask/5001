"""
    CS5001_5003 Fall 2023 San Jose
    Midterm Exam
    Q3. Squares.py

    Using for loops, write 2 functions, square_in_place and square_by_copying.
    They should each take 1 argument, a list of numbers. No validation required
    Each should return a corresponding list, but with each element squared.
    The first one should modify the original list, saving memory.
    The second one should make a copy, preserving the original list.
    One test case has been provided. Additional testing is not required today.
"""


# Your two function definitions here:
def square_in_place(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i] * my_list[i]
    return my_list
    

def square_by_copying(my_list):
    copy = my_list.copy()
    for i in range(len(copy)):
        copy[i] = copy[i] * copy[i]
    return copy


def main():
    """ Minimal test cases provided, to save time on midterm """
    lst1_original = [2, 4, 6, 8, 10]
    print("Original list:", lst1_original)
    print("Copy-Modified list:", square_by_copying(lst1_original))
    print("Original list:", lst1_original)

    lst1_modified = square_in_place(lst1_original)
    print("In-Place-Modified list:", lst1_modified)
    print("Original list:", lst1_original)


if __name__ == '__main__':
    main()
