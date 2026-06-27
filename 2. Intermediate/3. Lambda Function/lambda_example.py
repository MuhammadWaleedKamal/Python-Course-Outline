"""
Lambda function example.
Uses lambda expressions for sorting and tip calculation.
"""

products = ["chair", "desk", "lamp", "shelf"]
print(sorted(products, key=lambda item: len(item)))

calculate_tip = lambda amount, rate=0.15: amount * rate
print(f"Tip on $80 order: ${calculate_tip(80):.2f}")

# Exercises:
# 1. Sort products in reverse alphabetical order with lambda.
# 2. Write a lambda for a 10% discount.
# 3. Use lambda with map() to calculate discounted prices.
