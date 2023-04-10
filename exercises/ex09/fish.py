"""File to define Fish class."""


class Fish:
    """Fish in river get eat by bear, not yum."""
    # attributes
    age: int

    def __init__(self):
        """Initialize attribute values."""
        self.age: int = 0
    
    def one_day(self):
        """Fish age once per day."""
        self.age += 1
        return None