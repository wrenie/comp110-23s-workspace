"""The test file for dictionary exercise."""

__author__ = "730466370"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_short() -> None:
    """Tests for regular short usage of a typical dictionary of invert."""
    my_dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(my_dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_long() -> None:
    """Tests for regular long dict usage of the invert function."""
    my_dictionary: dict[str, str] = {'meow': 'lk', 'chirp': 'bok', 'meong': 'min', 'howl': 'bc', 'oink': 'bin'}
    assert invert(my_dictionary) == {'lk': 'meow', 'bok': 'chirp', 'min': 'meong', 'bc': 'howl', 'bin': 'oink'}


def test_invert_empty() -> None:
    """Tests for blank dictionary of invert function."""
    my_dictionary: dict[str, str] = {}
    assert invert(my_dictionary) == {}


def test_favorite_color_tie() -> None:
    """Tests favorite_color for when there's a tie in counts."""
    my_dictionary: dict[str, str] = {'bok': 'yellow', 'chan': 'blue', 'hannie': 'blue', 'innie': 'yellow'}
    assert favorite_color(my_dictionary) == 'yellow'


def test_favorite_color_regular() -> None:
    """Tests favorite_color using a regular, typical use dictionary."""
    my_dictionary: dict[str, str] = {'bok': 'yellow', 'chan': 'blue', 'hannie': 'blue'}
    assert favorite_color(my_dictionary) == 'blue'


def test_favorite_color_empty() -> None:
    """Tests favorite_color when the input dict is empty."""
    my_dictionary: dict[str, str] = {}
    assert favorite_color(my_dictionary) == ''


def test_count_empty() -> None:
    """Tests count function when the input is empty."""
    my_list: list[str] = []
    assert count(my_list) == {}


def test_count_long() -> None:
    """Tests count function with a long typical dict."""
    my_list: list[str] = ['bok', 'bok', 'apple', 'banana', 'apple', 'bok', 'blueberry', 'banana']
    assert count(my_list) == {'bok': 3, 'apple': 2, 'banana': 2, 'blueberry': 1}


def test_count_no_duplicates() -> None:
    """Tests count function when there are no duplicates."""
    my_list: list[str] = ['bok', 'apple', 'banana', 'blueberry']
    assert count(my_list) == {'bok': 1, 'apple': 1, 'banana': 1, 'blueberry': 1}