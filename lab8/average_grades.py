
"""
    CS5001_5003 Fall 2023 SV
    Lab08
    Xinrui Yi
"""
import os


def average_grades(my_file):
    """
        this function receives a file as a parameter and reads
        grades from the file and returns the average of the grades
    """
    try:
        with open(my_file, 'r') as file:
            # read file
            grades = []
            for line in file:
                line = line.strip()
                if len(line) > 0:
                    grades.append(float(line))
            if len(grades) == 0:
                return 0.0
            else:
                print(sum(grades) / len(grades))
                return sum(grades) / len(grades)  
    except FileNotFoundError:
        print(f'File {my_file} was not found')
    except PermissionError:
        print(f'Permission denied for {my_file}')
    except OSError:
        print(f'Error occurred while reading {my_file}')
