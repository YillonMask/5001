"""
    CS5001_5003 Fall 2023 SV
    Lab07
    Xinrui Yi
"""


def is_bridge(course_number):
    """
        this function check the course number is in bridge list and 
        the input is integer. Otherwise raise TypeError.
    """
    bridge_class = [5001, 5002, 5003, 5004, 5005, 5008, 5009]
    if not isinstance(course_number, int):
        raise TypeError
    if course_number in bridge_class:
        return True
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    main()
