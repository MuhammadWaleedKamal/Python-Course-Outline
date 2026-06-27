"""
Map, filter, and reduce example.
Applies discounts and sums selected product prices.
"""

from functools import reduce

prices = [12.0, 25.5, 9.99, 32.0]
discounted = list(map(lambda p: p * 0.9, prices))
filtered = list(filter(lambda p: p >= 20, discounted))
total = reduce(lambda acc, p: acc + p, filtered, 0)

print("Discounted prices:", discounted)
print("Prices above $20:", filtered)
print(f"Total of filtered prices: ${total:.2f}")

# Exercises:
# 1. Change the discount rate to 15%.
# 2. Filter prices below $15 instead of above $20.
# 3. Use sum() instead of reduce().
