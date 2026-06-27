"""
Recursion example.
Calculates factorial to show how many ways items can be arranged.
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

items = 5
print(f"The number of ways to arrange {items} items is {factorial(items)}")

# Exercises:
# 1. Add input validation for non-negative integers.
# 2. Write a recursive Fibonacci function.
# 3. Print factorial values for numbers 1 through 6.
