"""File to define Bear class."""


class Bear:
    """Bear in river eat fish yum."""
    # bear attributes
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize attribute values."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self):
        """Bear gets hungry and ages by one each day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Makes changes to hunger score based on fish count (fight for bear rights to fish)!"""
        self.hunger_score += num_fish
        return None
