"""An exercise utilizing lists."""

__author__ = "730566370"


def all(number_list: list[int], number: int) -> bool:
    """Indicates whether or not all numbers in list are same as given integer."""
    idx: int = 0
    if len(number_list) == 0:
        return False
    while idx < len(number_list) - 1:
        if number_list[idx] != number:
            return False  # False otherwise or if the list is empty 
        else:
            idx += 1
    return True  # True if all numbers match the indicated number 


def max(number_list: list[int]) -> int:
    """Finds the greatest number in a list."""
    if len(number_list) == 0:
        raise ValueError("max() arg is an empty List")
    start: int = number_list[0]
    truth: bool = all(number_list, start)
    if truth is True:  # only one number in the list so the largest is the only value
        return start
    current_max: list[int] = list()
    idx: int = 0
    while idx < len(number_list) - 1:  # while we haven't reached the end of the list yet
        if len(current_max) == 0:  # we haven't begun sorting through the numbers yet
            num_1: int = number_list[idx]
            num_2: int = number_list[idx + 1]
            if num_1 > num_2:  # if the first number is greater than the second, make it the max 
                current_max.append(num_1)
            else:  # the second number is greater
                current_max.append(num_2)
        idx += 1
        if current_max[0] < number_list[idx]:  # if the current max is less than the next number
            current_max[0] = number_list[idx]  # make the next number the new max
    maximum = current_max[0]  # turn the list into a single integer
    return maximum


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks whether every element at every index is equal in both lists."""
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    while idx < len(list_1) and idx < len(list_2):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True