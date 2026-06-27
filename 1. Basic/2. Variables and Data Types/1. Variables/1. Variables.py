"""
Variables example.
Calculates the total cost of a classroom supply order.
"""

product_name = "Notebook"
quantity = 12
price_per_unit = 2.50

total_cost = quantity * price_per_unit

print(f"Item: {product_name}")
print(f"Quantity ordered: {quantity}")
print(f"Unit price: ${price_per_unit:.2f}")
print(f"Total cost: ${total_cost:.2f}")

# Exercises:
# 1. Change the item and quantity for a different purchase.
# 2. Add a second item and compute the combined total cost.
# 3. Print a special message if the total cost is above $30.
