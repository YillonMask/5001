"""
    CS5001_5003 Fall 2023 SV
    Lab09
    Xinrui Yi
"""


def get_dictionary_string(my_dict):
    """
        this function reveives a dictionary and returns the keys
        of the dictionary as a string with each value on its own line
    """
    result = []
    key_value = ''
    for k, v in my_dict.items():
        key_value = str(k) + ' - ' + str(v)
        result.append(key_value)
    key_string = '\n'.join(result)
    print(key_string)
    return key_string


def main():
    pass


if __name__ == '__main__':
    main()
