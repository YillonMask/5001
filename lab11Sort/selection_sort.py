''' Align Online CS5001
    Module 14 -- Efficiency
    Sample code -- implementation of selection sort
'''
import random


def selection_sort(things):
    '''
    Function: selection_sort -- sorting the elements of a list by inserting
                                each element into a list in order
    Parameters:
       things -- the elements to be sorted
    Returns a new list with all of the elements in sorted order
    '''
    for i in range(len(things) - 1):
        # select the next element by finding it in things
        min = i
        for j in range(i + 1, len(things)):
            if things[j] < things[min]:
                min = j
        things[i], things[min] = things[min], things[i]
    return things


def main():
    '''
    Function: main -- driver program for selection_sort
    '''
    my_list = [i for i in range(100)]
    random.shuffle(my_list)
    print(my_list)
    sorted_list = selection_sort(my_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
