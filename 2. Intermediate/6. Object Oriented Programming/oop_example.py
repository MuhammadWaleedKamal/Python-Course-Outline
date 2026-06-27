"""
Object oriented programming example.
Defines a Product class with discount methods.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, rate):
        return self.price * (1 - rate)

    def __str__(self):
        return f"{self.name} at ${self.price:.2f}"

item = Product("Backpack", 49.99)
print(item)
print(f"Price after 20% discount: ${item.apply_discount(0.20):.2f}")

# Exercises:
# 1. Add a method that increases the price by a markup percentage.
# 2. Create another Product and print both objects.
# 3. Add a stock quantity attribute and print it.
