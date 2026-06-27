"""
Math module example.
Uses math functions to calculate a circle area and rounding.
"""

import math

radius = 7
area = math.pi * radius ** 2
print(f"Circle radius: {radius}")
print(f"Area: {area:.2f}")
print(f"Rounded area: {math.ceil(area)}")
print(f"Square root of area: {math.sqrt(area):.2f}")

# Exercises:
# 1. Compute circumference using math.pi.
# 2. Use math.floor() on the area.
# 3. Add a function that returns the diameter.
