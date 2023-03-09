"""The definition of the functions for exercise 5."""

__author__ = "730566370"


def only_evens(list_input: list[int]) -> list[int]:
    """Given a list of numbers, returns a list with only the even numbers."""
    idx: int = 0
    list_output: list[int] = list()
    for idx in range(0, len(list_input)):
        if list_input[idx] % 2 == 0:
            list_output.append(list_input[idx])
    return list_output


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, returns a list containing both the first and second list."""
    list_output: list[int] = list()
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(list1):
        list_output.append(list1[idx1])
        idx1 += 1
    while idx2 < len(list2):
        list_output.append(list2[idx2])
        idx2 += 1
    return list_output
        

def sub(list_input: list[int], start: int, end: int) -> list[int]:
    """Given a list and a range, returns a list with the values in the range (non-inclusive of the end value)."""
    idx: int = 0
    list_output: list[int] = list()
    if start < 0:
        start == 0
    while idx < len(list_input):
        if idx >= start and idx < end:  # if the index is greater than or equal to the start index but less than the end index
            list_output.append(list_input[idx])
        idx += 1
    return list_output