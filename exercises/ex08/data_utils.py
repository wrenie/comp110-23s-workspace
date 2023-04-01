"""The utilities for data wrangling assignment ex08."""

__author__ = "730566370"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads CSV file and returns a list of dicts containing the info."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:  # for each idx (row) in table
        result.append(row[column])  # index shows what dictionary there is, want to access the VALUE of the associated key
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data table so that it is a dict with column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]  # loop through keys of one row of table
    for key in first_row:  # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column based table with only the first N rows of data for each column."""
    result_dict: dict[str, list[str]] = {}
    for column in column_table:
        list_values: list[str] = []
        if N > len(column_table[column]):
            for idx in range(0, len(column_table[column])):
                values: str = (column_table[column])[idx]
                list_values.append(values)
        else:
            for idx in range(0, N):
                values = (column_table[column])[idx]
                list_values.append(values)
        result_dict[column] = list_values
    return result_dict


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result_dict: dict[str, list[str]] = {}
    for column in column_names:
        result_dict[column] = column_table[column]
    return result_dict


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table by combining two column based data tables."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column2 in table2:
        if column2 in result:
            idx: int = 0
            while idx < len(table2[column2]):
                result[column2].append((table2[column2])[idx])  # appending with the value of the list associated with key 'column2' in table2
                idx += 1
        else:
            result[column2] = table2[column2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of each key and returns as dict."""
    result: dict[str, int] = {}
    for idx in range(0, len(values)):  # staying within the range of the list
        if values[idx] in result:
            result[values[idx]] += 1
        else:
            result[values[idx]] = 1
    return result