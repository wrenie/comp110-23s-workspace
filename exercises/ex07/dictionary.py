"""The dictionary for exercise 7."""

__author__ = "730566370"


def invert(merr_webb: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts the order of the keys."""
    result: dict[str, str] = {}
    past_key = ""
    for key in merr_webb:
        if past_key in merr_webb:
            if merr_webb[key] == merr_webb[past_key]:  # if more than 1 value is the same, raise keyerror
                raise KeyError("There cannot be more than one of the same key.")
        old_value: str = merr_webb[key]
        result[old_value] = key  # old key becomes new value and old value becomes new key
        past_key = key
    return result


def favorite_color(name_color: dict[str, str]) -> str:
    """Returns the most frequent color marked as a favorite."""
    count: dict[str, int] = {}
    result: str = ""
    past_key: str = ""
    for name in name_color:  # count the colors
        if name_color[name] in count:  # if the color is already there
            count[(name_color[name])] += 1
        else:
            count[(name_color[name])] = 1 
    print(count)
    for color in count:  # going thru the colors and their counts
        if past_key in count:  # if this isn't the first key
            if count[color] > count[past_key]:  # if the value of the current key is greater than the last key
                result = color
            elif count[color] < count[past_key]:
                result = past_key
            if count[color] == count[past_key]:
                result = past_key
        else:  # if this is the first key
            result = color
        past_key = color
    return result


def count(input: list[str]) -> dict[str, int]:
    """Returns a dict with the count of each item in the list."""
    result: dict[str, int] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result