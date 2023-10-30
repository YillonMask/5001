"""
    CS5001_5003 Fall 2023 SV
    Lab06
    Xinrui Yi
"""


def compare_lists(nums1, nums2):
    """
        this function reveives two lists of integer values
        return true if the elements in first list are contained
        in second list
    """
    for num in nums1:
        if num not in nums2:
            return False
    return True


def main():
    pass


if __name__ == '__main__':
    main()
