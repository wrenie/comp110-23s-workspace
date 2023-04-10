"""Lessontest test."""

from lessons.sum import sum

def test_empty() -> None:
    assert sum([]) == 0.0

def test_one_number() -> None:
    assert sum([1.0]) == 1.0

def test_multiple() -> None:
    test_variable: list[float] = [1.0, 2.0, 1.0]
    assert sum(test_variable) == 4.0

def test_negatives() -> None:
    test_list: list[float] = [-1.0, 2.0, -1.0]
    assert sum(test_list) == 0.0