"""
    CS5001_5003 Fall 2023 SV
    Lab09
    Xinrui Yi
"""


def get_key_string(my_dict):
    """
        this function reveives a dictionary and returns the values
        of the dictionary as a string with each value on its own line
    """
    result = []
    for k, v in my_dict.items():
        result.append(str(k))
    key_string = '\n'.join(result)
    print(key_string)
    return key_string


def main():
    pass


if __name__ == '__main__':
    main()
