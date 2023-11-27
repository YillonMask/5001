''' Align Online CS5001
    Module 14 -- Efficiency
    Sample code -- implementation of bubble sort
'''
import random


def bubble_sort(things):
    '''
    Function: bubble_sort -- sorting the elements of a list by swapping
                             two consecutive elements that are out of order
    Parameters:
       things -- the elements to be sorted
    Returns a new list with all of the elements in sorted order
    '''
    swapped = True
    while swapped is True:
        swapped = False
        for i in range(0, len(things) - 1):
            if things[i] > things[i + 1]:
                things[i], things[i + 1] = things[i+ 1], things[i]
                swapped = True


def main():
    '''
    Function: main -- driver program for bubble_sort
    '''
    my_list = [i for i in range(100)]
    random.shuffle(my_list)
    print(my_list)
    bubble_sort(my_list)
    print(my_list)


if __name__ == "__main__":
    main()
