"""Using pizza objects."""

from pizza import Pizza

my_pizza: Pizza = Pizza("small", 3, False)
eleanor_pizza: Pizza = Pizza("medium", 3, True)

# def price(pizza_order: Pizza) -> float:
#     """Calculate and return cost of pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else:
#         cost = 5.0
#     # charge per topping
#     cost += 0.75*pizza_order.toppings
#     if pizza_order.gluten_free:
#         cost += 1.00
#     return cost

print(eleanor_pizza.price())
print(my_pizza.price())