"""Practice Defining and Writing Own Functions."""

def my_min(number1: int, number2: int) -> int:
    """Returns the minimum value out of two numbers"""
    if number1 <= number2:
        return number1
    else: #number1 is greater than number 2
        return number2

min_number: int = my_min(1,10)
print(min_number)

