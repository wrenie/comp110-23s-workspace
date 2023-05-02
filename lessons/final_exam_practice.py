"""Practice for final exam."""

def free_biscuits(teams_score: dict[str, list[int]]) -> dict[str, bool]:
    """Total to over 100 points scored."""
    result: dict[str, bool] = {}
    for game in teams_score:
        point_list: list[int] = teams_score[game]
        total_points: int = 0
        idx: int = 0
        while idx < len(point_list):
            total_points += point_list[idx]
            idx += 1
        if total_points >= 100:
            result[game] = True
        else:
            result[game] = False
    return result

biscuit: dict[str, list[int]] = {}
biscuit["UNCvsDuke"] = [38, 20, 42]
biscuit["UNCvsState"] = [9, 51, 16, 23]
print(free_biscuits(biscuit))

class HotCocoa:

    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, whip: bool, flavor: str, marsh_count: int, sweet_val: int):
        """Construct HotCocoa object."""
        self.has_whip = whip
        self.flavor = flavor
        self.marshmallow_count = marsh_count
        self.sweetness = sweet_val

    def mallow_adder(self, factor: int) -> None:
        """Increase mallow count by factor and increase sweetness value by two times factor."""
        self.marshmallow_count += factor
        self.sweetness += (2 * factor)
    
    def calorie_count(self) -> float:
        """Count the calories in the cocoa."""
        calories: float = 0.0
        if self.flavor == "peppermint" or self.flavor == "vanilla":
            calories += 30.0
        else:
            calories += 20.0
        if self.has_whip == True:
            calories += 100.0
        calories += (self.marshmallow_count / 2.0)
        return calories

def rainbow(string: str) -> str:
    """Exam prompt: return longest streak count and value."""
    current_val: str = ""
    current_streak: int = 0
    long_val: str = ""
    long_streak: int = 0
    idx: int = 0
    while idx < len(string):
        if idx == 0:
            current_val = string[0]
            current_streak = 1
            long_streak = 1
            long_val = string[0]
        else:
            if current_streak >= long_streak:
                long_streak = current_streak
                long_val = current_val
            current_val = string[idx]
            if current_val == string[idx - 1]:
                current_streak += 1
            else:
                current_streak = 1
            if current_streak >= long_streak:
                long_streak = current_streak
                long_val = current_val
        idx += 1
    return f"{long_streak}{long_val}"

print(rainbow("aaaa  b ccc dddd"))
        