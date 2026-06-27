"""
Break and continue example.
Processes a list of orders while skipping cancelled items.
"""

orders = ["notebook", "cancelled", "pen", "pencil", "cancelled", "stapler"]
processed = 0
capacity = 3

for order in orders:
    if order == "cancelled":
        print("Skipping cancelled order")
        continue
    print(f"Processing order: {order}")
    processed += 1
    if processed >= capacity:
        print("Reached daily processing capacity.")
        break

# Exercises:
# 1. Count how many cancelled orders were skipped.
# 2. Allow urgent orders to continue even after capacity is reached.
# 3. Print a summary of processed and skipped orders.
