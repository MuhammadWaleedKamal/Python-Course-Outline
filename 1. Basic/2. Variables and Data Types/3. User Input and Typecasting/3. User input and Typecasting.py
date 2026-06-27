"""
User input and typecasting example.
Reads shopping order details and calculates the total cost.
"""

customer_name = input("Enter customer name: ")
item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total_price = quantity * unit_price

print(f"Customer: {customer_name}")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Total price: ${total_price:.2f}")

# Exercises:
# 1. Add a discount percentage and calculate the final price.
# 2. Validate that the quantity is a positive integer.
# 3. Print a message if the total price exceeds $100.
