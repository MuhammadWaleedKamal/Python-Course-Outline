"""
Generators and iterators example.
Creates order IDs for a shipping system.
"""

def order_id_generator(start, count):
    current = start
    for _ in range(count):
        yield current
        current += 1

for order_id in order_id_generator(1001, 5):
    print(f"New order ID: {order_id}")

# Exercises:
# 1. Modify the generator to skip every third ID.
# 2. Use iter() and next() to retrieve the first two IDs.
# 3. Create a generator for odd-numbered IDs.
