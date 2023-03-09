"""VS code follow along."""

def sum(list1: list[float]) -> float:
    """Sums all of the floats in a list."""
    sum_output: float = 0.0
    for idx in list1:
        sum_output += idx
    return sum_output