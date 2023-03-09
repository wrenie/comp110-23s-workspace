"""The testing site for the functions for exercise 5 utils."""

__author__ = "730566370"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_empty() -> None:
    """Tests the only_evens function when the input list is empty."""
    test_input: list[int] = []
    assert only_evens(test_input) == []


def test_only_evens_all_odds() -> None:
    """Tests the only_evens function when the input has all odd numbers."""
    test_input: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(test_input) == []


def test_only_evens_combine() -> None:
    """Tests the only_evens function when the input has a combination of even and odd numbers."""
    test_input: list[int] = [1, 2, 5, 7, 10]
    assert only_evens(test_input) == [2, 10]


def test_concat_empty() -> None:
    """Tests the concat function when the input is empty."""
    test_input1: list[int] = []
    test_input2: list[int] = []
    assert concat(test_input1, test_input2) == []


def test_concat_order1() -> None:
    """Tests the concat function when the input lists are in one order."""
    test_input1: list[int] = [2, 4, 6, 8, 10]
    test_input2: list[int] = [1, 3, 5, 7, 9]
    assert concat(test_input1, test_input2) == [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]


def test_concat_order2() -> None:
    """Tests the concat function when the input lists are in another order."""
    test_input2: list[int] = [2, 4, 6, 8, 10]
    test_input1: list[int] = [1, 3, 5, 7, 9]
    assert concat(test_input1, test_input2) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def test_sub_empty() -> None:
    """Tests the sub function when the input is empty."""
    test_input: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(test_input, start, end) == []


def test_sub_out_bounds() -> None:
    """Tests the sub function when the start and end values are out of the range of list index values."""
    test_input: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 7
    end: int = 8
    assert sub(test_input, start, end) == []


def test_sub_negative() -> None:
    """Tests when input has negative start and end values"""
    test_input: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = -1
    end: int = 4
    assert sub(test_input, start, end) == [1,2,3,4]


def test_sub_normal_list() -> None:
    """Tests the sub function with a normal list, with start and end values within the range of the list."""
    test_input: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 1
    end: int = 4
    assert sub(test_input, start, end) == [2, 3, 4]