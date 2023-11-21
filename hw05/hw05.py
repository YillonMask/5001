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


"""
The following function shows a SyntaxError, which is that "(" was not close
To fix this SyntaxError, we can close the parenthesis by adding ")"
at the end of code
def syntax_error():
    print("Hello, World!
"""


def type_error(my_set):
    # set
    if not isinstance(my_set, set):
        raise TypeError(f'The file "{my_set}" is not a set')


def value_error(numbers, number_remove):
    try:
        numbers.remove(number_remove)
    except:
        raise ValueError(f"The element {number_remove} is not in list {numbers}")


def name_error():
    try:
        print(my_undifined_variable)
    except:
        raise NameError(f"The name {my_undifined_variable} is not defined")


def file_not_found_error(file_name):
    # read dictionary from .json file
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f'The file "{file_name}" does not exist.')


def index_error(my_list, index):
    try:
        num = my_list[index]
        return num
    except IndexError:
        raise IndexError(f'The index "{index}" is out of range of list {my_list}')


def key_error(my_dict, key):
    # dictionary
    try:
        value = my_dict[key]
        return value
    except KeyError:
        raise KeyError(f"The key '{key}' does not exist in the dictionary {my_dict}")


def zero_division_error(a, b):
    if b == 0:
        raise ZeroDivisionError("The divisor 'b' cannot be zero")
    else:
        return a / b


def attribute_error(nums, append_num):
    try:
        nums.append(append_num)
    except AttributeError:
        raise AttributeError(
            f"The 'str' objects {nums}, does not have attribute 'append'."
        )


def os_error(file_not_permit):
    try:
        with open(file_not_permit, "w") as file:
            data = json.load(file)
            return data
    except OSError:
        raise OSError(f'OSError occured when opens "{file_not_permit}".')


def import_error(my_module):
    try:
        import my_module
    except ImportError:
        raise ImportError(f"The module {my_module} does not exist")


def logic_error(nums):
    result = 0
    n = 0
    while n < len(nums) - 1:
        result += nums[n]
        n += 1
    return result


def main():
    try:
        my_set = [1, 2, 3]
        type_error(my_set)
    except TypeError as e:
        print("TypeError:", e)
    try:
        zero_division_error(1, 0)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    try:
        file_not_found_error("my_dict")
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)
    try:
        my_dict = {"a": 1, "b": 2, "c": 3}
        value = key_error(my_dict, "d")
    except KeyError as e:
        print("KeyError:", e)
    try:
        my_list = [0, 1, 2]
        index_error(my_list, 3)
    except IndexError as e:
        print("IndexError:", e)
    try:
        numbers = [1, 2, 3]
        numbers_remove = 4
        value_error(numbers, numbers_remove)
    except ValueError as e:
        print("ValueError:", e)
    try:
        name_error()
    except NameError as e:
        print("NameError:", e)
    try:
        nums = "12345"
        append_num = 6
        attribute_error(nums, append_num)
    except AttributeError as e:
        print("AttributeError:", e)
    try:
        os_error("somefile.txt")
    except OSError as e:
        print("OSError:", e)
    try:
        my_module = None
        import_error(my_module)
    except ImportError as e:
        print("ImportError:", e)
    logic_error_nums = [1, 2, 3, 4]
    logic_error_sum = logic_error(logic_error_nums)
    print(
        f"Logic Error: the actual sum is {sum(logic_error_nums)}"
        f"but we got {logic_error_sum}"
    )


if __name__ == "__main__":
    main()
