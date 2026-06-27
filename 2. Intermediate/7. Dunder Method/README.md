# Dunder Method

Dunder methods, also called magic methods, are special methods in Python that start and end with double underscores like `__init__`, `__str__`, and `__len__`.

They allow objects to behave like built-in Python types.

## Common Dunder Methods

- `__init__()` - Initializes an object
- `__str__()` - Defines how an object is displayed as text
- `__len__()` - Returns the length of an object
- `__add__()` - Supports the `+` operator
- `__eq__()` - Supports equality comparison

## Example

```python
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Shopping Cart: {self.items}"

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)

cart1 = ShoppingCart(["Pen", "Notebook"])
cart2 = ShoppingCart(["Book"])

print(cart1)
print(len(cart1))
print(cart1 + cart2)
```

## Real World Use

Dunder methods are used in real applications such as:

- Shopping carts in e-commerce websites
- Bank account objects
- Student or employee records
- Custom data structures

## Exercises

1. Add a `__contains__()` method to check whether an item exists in the cart.
2. Create a new cart and compare two carts using `__eq__()`.
3. Add a method that removes an item from the cart and print the updated cart.
