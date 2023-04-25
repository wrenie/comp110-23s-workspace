"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730566370"


class Simpy:
    """Simpy, for adding, multiplying and power-ing floats."""
    
    values: list[float]

    def __init__(self, values: list[float]):
        """Assign values from call."""
        self.values = values

    def __str__(self) -> str:
        """Magical str method."""
        result: str = "Simpy("
        result += str(self.values)
        result += ")"
        return result
    
    def fill(self, fill_val: float, count: int) -> None:
        """Mutates simpy to be the indicated values."""
        final: list[float] = []
        idx: int = 0
        while idx < count:
            final.append(fill_val)
            idx += 1
        self.values = final

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a range of floats using start, stop and step values."""
        assert step != 0.0
        result: list[float] = []
        idx: float = start
        while idx != stop:
            result.append(idx)
            idx += step
        self.values = result

    def sum(self) -> float:
        """Sum of Simpy."""
        result: float = 0.0
        for value in self.values:
            result += value
        return result
    
    def __add__(self, additive: Union[float, Simpy]) -> Simpy:
        """Magic method for addition."""
        result: Simpy = Simpy([])
        if type(additive) is not float:  # additive is a Simpy
            assert len(self.values) == len(additive.values)
            idx: int = 0
            while idx < len(additive.values):
                total: float = additive.values[idx] + self.values[idx]
                result.values.append(total)
                idx += 1
        else:  # additive is a float
            idx: int = 0
            while idx < len(self.values):
                add: float = self.values[idx]
                total: float = additive + add
                result.values.append(total)
                idx += 1
        return result
    
    def __pow__(self, power: Union[float, Simpy]) -> Simpy:
        """Magic method for power functions."""
        result: Simpy = Simpy([])
        if type(power) is not float:  # power is a Simpy
            assert len(self.values) == len(power.values)
            idx: int = 0
            while idx < len(power.values):
                total: float = self.values[idx] ** power.values[idx]
                result.values.append(total)
                idx += 1
        else:  # power is a float
            idx: int = 0
            while idx < len(self.values):
                add: float = self.values[idx]
                total: float = add ** power
                result.values.append(total)
                idx += 1
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Make list of bool that shows whether a Simpy is equal to a float or another Simpy."""
        result: list[bool] = []
        if type(rhs) is not float:  # rhs is a Simpy
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == rhs.values[idx]:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        else:  # rhs is a float
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Override greater than function to produce a list of bool."""
        result: list[bool] = []
        if type(rhs) is not float:  # rhs is a Simpy
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > rhs.values[idx]:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        else:  # rhs is a float
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use [] to get item from values list."""
        if type(rhs) is not int:  # if rhs is a list of bool
            result: Simpy = Simpy([])
            idx: int = 0
            while idx < len(rhs):
                if rhs[idx] is True:
                    result.values.append(self.values[idx])
                idx += 1
        else:  # rhs is an int
            result: float = self.values[rhs]
        return result
    # TODO: Your constructor and methods will go here.