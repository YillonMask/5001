"""
    CS5001_5003 Fall 2023 SV
    In-class Exercise -- Day Number
    Xinrui Yi
"""


def day_number(my_input):
    """
        this function
    """
    my_dict = {"SUN": 0,
               "MON": 1,
               "TUE": 2,
               "WED": 3,
               "THU": 4,
               "FRI": 5,
               "SAT": 6}
    # make the case of the key string not matter
    upper_day = my_input.upper()
    # make extraneous whitespace before or after the key string not matter
    strip_day = upper_day.strip()
    #Accept shortened versions of the days names
    day = strip_day[:3]
    print(day)
    print(my_dict[day])


def main():
    day_number(" sUnday  ")
    day_number(" sAt  ")


if __name__ == '__main__':
    main()
