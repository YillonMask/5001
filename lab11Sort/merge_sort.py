''' Align Online CS5001
    Module 14 -- Efficiency
    Sample code -- implementation of insertion sort
'''
import random


def merge_sort(cards):
    '''
    Function: merge_sort -- sorting the elements of a list by inserting
                            each element into a list in order
    Parameters:
       cards -- the elements to be sorted
    Returns a new list with all of the elements in sorted order
    '''
    # base case is just a single card
    if len(cards) == 1:
        return cards
    else:
        # find the midpoint of this
        mid = len(cards) // 2
        # sort the cards in the first half of the deck
        sorted_top = merge_sort(cards[0:mid])
        # sort the cards in the second half of the deck
        sorted_bottom = merge_sort(cards[mid:])
        # merge them together and regurn
        return merge(sorted_top, sorted_bottom)


def merge(deck1, deck2):
    '''
    Function: merge -- merge two sorted lists together in sorted order
    Parameters:
       deck1 -- the first sorted list
       deck2 -- the second sorted list
    Returns a new list that contains all of the elements of deck1 and deck2
    '''
    i1 = 0
    i2 = 0
    merged = []
    while i1 < len(deck1) and i2 < len(deck2):
        # pick the lowest card from the top of the two decks
        if deck1[i1] < deck2[i2]:
            merged.append(deck1[i1])
            i1 += 1
        else:
            merged.append(deck2[i2])
            i2 += 1
    # if one of the decks runs out, just add the rest of them
    if i1 < len(deck1):
        merged.extend(deck1[i1:])
    else:
        merged.extend(deck2[i2:])
    return merged


def main():
    '''
    Function: main -- driver program for merge_sort
    '''
    my_list = [i for i in range(100)]
    random.shuffle(my_list)
    print(my_list)
    sorted_list = merge_sort(my_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
