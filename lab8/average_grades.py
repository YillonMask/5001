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
            print(grades)
            sum = 0.0
            count = 0.0
            for grade in grades:
                sum += float(grade)
                count += 1
            return sum / count if count != 0 else 0.0
    except PermissionError:
        print(f"Permission denied for {my_file}")
        
    except OSError:
        print(f"Error occurred while reading {my_file}")
        
    except FileNotFoundError:
        print(f"File {my_file} was not found")
        


def main():
    average_grades("grades.txt")


if __name__ == '__main__':
    main()
