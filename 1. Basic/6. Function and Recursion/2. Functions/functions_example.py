"""
Functions example.
Prints a simple invoice using reusable helper functions.
"""

def calculate_total(price, quantity):
    return price * quantity

def print_invoice(item, price, quantity):
    total = calculate_total(price, quantity)
    print(f"{item}: {quantity} x ${price:.2f} = ${total:.2f}")

print_invoice("Notebook", 3.50, 5)
print_invoice("Pen", 1.20, 10)

# Exercises:
# 1. Add a function to apply sales tax to the invoice.
# 2. Create a function that prints a receipt summary for multiple items.
# 3. Add a function that calculates a discount amount.
