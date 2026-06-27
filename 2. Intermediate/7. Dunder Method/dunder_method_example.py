"""
Real world example of dunder methods.
This example uses a ShoppingCart class to simulate an online shopping cart.
"""

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        if not self.items:
            return "Shopping Cart is empty"
        return f"Shopping Cart: {self.items}"

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)

    def __contains__(self, item):
        return item in self.items


cart1 = ShoppingCart(["Pen", "Notebook"])
cart2 = ShoppingCart(["Book"])

print(cart1)
print("Number of items:", len(cart1))
print("Book in cart1:", "Book" in cart1)

combined_cart = cart1 + cart2
print("Combined Cart:", combined_cart)

# Exercises:
# 1. Add a __eq__() method to compare two carts.
# 2. Create another cart and check whether it is equal to cart1.
# 3. Add a method to remove an item from the cart and print the updated cart.
