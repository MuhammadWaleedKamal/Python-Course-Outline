"""
Function arguments example.
Demonstrates positional, keyword, and default arguments in a customer greeting.
"""

def greet_customer(name, greeting="Hello", store_name="Corner Store"):
    return f"{greeting}, {name}! Welcome to {store_name}."

print(greet_customer("Aisha"))
print(greet_customer("Bilal", greeting="Good afternoon"))
print(greet_customer("Clara", store_name="City Market"))

# Exercises:
# 1. Add a keyword argument for customer membership level.
# 2. Call greet_customer() using only keyword arguments.
# 3. Change the default greeting to "Welcome".
