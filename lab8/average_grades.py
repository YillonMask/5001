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
            grades = file.readlines()
            grades = [float(grades.strip()) for grade in grades 
                      if grade.strip().isdigit()]
            return sum(grades) / len(grades) if grades else None    
    except PermissionError:
        print(f"Permission denied for {my_file}")
        return None
    except OSError:
        print(f"Error occurred while reading {my_file}")
        return None
    except FileNotFoundError:
        print(f"File {my_file} was not found")
        return None
