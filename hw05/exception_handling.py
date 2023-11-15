"""
    CS5001_5003 Fall 2023 SV
    HW5
    Xinrui Yi
    This program will provide practice in exception handling, 
    file input/output using JSON format, dictionaries, and sets. 
    Specifically, create one function per type of error, 
    including 10 different exceptions being raised, 
    plus one other function containing a logical error (not an exception).
"""
import json


#def syntax_error():



def type_error(my_set):
    # set
    if not isinstance(my_set, set):
        raise TypeError(f'The file "{my_set}" is not set')


##def value_error():


#def name_error():


def file_not_found_error(file_name):
    # read dictionary from .json file
    try:
        with open(file_name,'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f'The file "{file_name}" does not exist.')

def index_error(my_list, index):
    try:
        num = my_list[index]
    except IndexError:
        raise IndexError(f'The index "{index}" is out of range of list {my_list}')


def key_error(my_dict, key):
    # dictionary
    try:
        value = my_dict[key]
    except KeyError:
        raise KeyError(f"The key '{key}' does not exist in the dictionary {my_dict}")


def zero_division_error(a, b):
    if b == 0:
        raise ZeroDivisionError(f"The divisor 'b' cannot be zero")
    else:
        return a / b


#def attribute_error():


#def import_error():





def main():
    try:
        my_set = [1, 2, 3]
        type_error(my_set)
    except TypeError as e:
        print(e)
    try:
        zero_division_error(1, 0)
    except ZeroDivisionError  as e:
        print(e)
    try:
        file_not_found_error("my_dict")
    except FileNotFoundError as e:
        print(e)
    try:
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        value = key_error(my_dict, 'd')
    except KeyError as e:
        print(e)
    try:
        my_list = [0, 1, 2]
        index_error(my_list, 3)
    except IndexError as e:
        print(e)



if __name__ == '__main__':
    main()
