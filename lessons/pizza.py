"""Practice with classes and object oriented programming."""

class Pizza:

    # attributes
    size: str # small or large
    toppings: int # number of toppings
    gluten_free: bool #  True if gf, false if not

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # it returns "self"
    
    def price(self) -> float:
        """Calculate and return cost of pizza."""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else:
            cost = 5.0
        # charge per topping
        cost += 0.75*self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost