"""Challenge Question 7."""

from __future__ import annotations

class Point:
    """Model a 2D point."""

    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        self.x *= factor
        self.y *= factor

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __add__(self, additive: float) -> Point:
        new_x: float = self.x + additive
        new_y: float = self.y + additive
        result: Point = Point(new_x, new_y)
        return result

pointy: Point = Point(2.0, 3.0)
print(pointy)
b: Point = (pointy + 3.0)
print(b)