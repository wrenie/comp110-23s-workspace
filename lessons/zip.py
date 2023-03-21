"""Challenge Question 4: Writing dictionary functions."""

__author__ = "730566370"

def zip(key: list[str], values: list[int]) -> dict[str, int]:
    """Produces a dict from two lists where the first list is the key and the second list is the index."""
    merriam_web: dict[str, int] = dict()  # named after the great merriam webster
    idx: int = 0
    if len(key) != len(values):
        return dict()
    if len(key) == 0 or len(values) == 0:
        return dict()
    while idx < len(key):
        merriam_web[key[idx]] = values[idx]
        idx += 1
    return merriam_web