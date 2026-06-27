# Arithmetic Operations

## What are Arithmetic Operations?

**Arithmetic operations** are mathematical calculations performed on numeric values. They include addition, subtraction, multiplication, division, and more.

## Basic Arithmetic Operators

### 1. Addition (+)
Adds two numbers

```python
x = 10 + 5       # 15
y = 3.5 + 2.1    # 5.6
result = 100 + 50  # 150
```

### 2. Subtraction (-)
Subtracts the second number from the first

```python
x = 10 - 5       # 5
y = 100 - 45     # 55
temperature = 20 - 10  # 10
```

### 3. Multiplication (*)
Multiplies two numbers

```python
x = 5 * 4        # 20
price = 12.50 * 3  # 37.50
area = 5 * 5     # 25
```

### 4. Division (/)
Divides the first number by the second (returns float)

```python
x = 20 / 4       # 5.0 (returns float)
y = 10 / 3       # 3.333...
total = 100 / 2  # 50.0
```

### 5. Floor Division (//)
Divides and returns the integer part (rounds down)

```python
x = 20 // 4      # 5
y = 10 // 3      # 3 (not 3.333)
remainder = 7 // 2  # 3
```

### 6. Modulo (%)
Returns the remainder of division

```python
x = 20 % 4       # 0 (no remainder)
y = 10 % 3       # 1 (remainder)
is_even = number % 2 == 0  # True if even
```

### 7. Exponentiation (**)
Raises a number to the power of another

```python
x = 2 ** 3       # 8 (2 to the power of 3)
y = 5 ** 2       # 25 (5 squared)
z = 10 ** -1     # 0.1 (10 to the power of -1)
```

## Operator Precedence (BODMAS)

Operations are evaluated in this order:

1. **B**rackets: ()
2. **O**rders (Exponents): **
3. **D**ivision and **M**ultiplication: / // *
4. **A**ddition and **S**ubtraction: + -

```python
result = 2 + 3 * 4          # 14 (not 20)
result = (2 + 3) * 4        # 20 (parentheses first)
result = 10 - 5 - 2         # 3 (left to right)
result = 2 ** 3 ** 2        # 512 (right to left for **)
```

## Assignment Operators with Arithmetic

Shorthand notation for operations:

```python
x = 10
x += 5      # x = x + 5  → 15
x -= 3      # x = x - 3  → 12
x *= 2      # x = x * 2  → 24
x /= 4      # x = x / 4  → 6.0
x //= 2     # x = x // 2 → 3
x %= 2      # x = x % 2  → 1
x **= 3     # x = x ** 3 → 1
```

## Real-World Examples

### Example 1: Calculate Total Bill
```python
item_price = 12.50
quantity = 4
tax_rate = 0.07

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

### Example 2: Calculate Average
```python
score1 = 85
score2 = 92
score3 = 78

average = (score1 + score2 + score3) / 3
print(f"Average score: {average:.2f}")
```

### Example 3: Temperature Conversion
```python
# Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Fahrenheit to Celsius
fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.2f}°C")
```

### Example 4: Check if Number is Even or Odd
```python
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

## Common Arithmetic Functions

```python
# Absolute value
abs(-10)              # 10
abs(5)                # 5

# Power (alternative to **)
pow(2, 3)             # 8
pow(5, 2)             # 25

# Sum of numbers
sum([1, 2, 3, 4, 5])  # 15

# Minimum/Maximum
min(5, 2, 8, 1)       # 1
max(5, 2, 8, 1)       # 8
```

## Floating Point Precision

```python
# Sometimes floating point can be imprecise
x = 0.1 + 0.2
print(x)              # 0.30000000000000004 (not exactly 0.3)

# Solution: Use rounding
x = round(0.1 + 0.2, 2)  # 0.3
print(x)
```

## Type Consistency in Arithmetic

```python
# Integer operations return integer (except division)
10 + 5        # 15 (int)
10 * 3        # 30 (int)
10 / 2        # 5.0 (float!)

# When mixing int and float, result is float
10 + 3.5      # 13.5 (float)
20 * 1.5      # 30.0 (float)
```

## Exercises

1. Calculate the area and perimeter of a rectangle
2. Convert temperature between Celsius and Fahrenheit
3. Calculate simple and compound interest
4. Find the remainder when dividing by 10
5. Calculate the cost of items with tax and discount
