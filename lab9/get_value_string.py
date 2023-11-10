"""
    CS5001_5003 Fall 2023 SV
    Lab09
    Xinrui Yi
"""


def get_value_string(my_dict):
    """
        this function reveives a dictionary and returns the values
        of the dictionary as a string with each value on its own line
    """
    result = []
    for k, v in my_dict.items():
        result.append(str(v))
    value_string = '\n'.join(result)
    print(value_string)
    return value_string


def main():
    pass


if __name__ == '__main__':
    main()
