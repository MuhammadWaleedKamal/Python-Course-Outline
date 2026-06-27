"""
Exception handling example.
Handles invalid user input for a product price.
"""

user_value = input("Enter a product price: ")
try:
    price = float(user_value)
    if price < 0:
        raise ValueError("Price cannot be negative")
    print(f"Price entered: ${price:.2f}")
except ValueError as error:
    print("Invalid input:", error)
finally:
    print("Price check complete.")

# Exercises:
# 1. Add a loop that asks again until valid input is provided.
# 2. Separate negative value handling into its own branch.
# 3. Print a friendly message when valid input is received.
