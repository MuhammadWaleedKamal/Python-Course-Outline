# Recursion

## What is Recursion?

A function calling itself.

## Recursive Function Structure

1. **Base Case**: Condition to stop recursion
2. **Recursive Case**: Function calls itself

```python
def factorial(n):
    if n <= 1:           # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
```

## Fibonacci Example
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Call Stack
```
factorial(5)
→ 5 * factorial(4)
→ 5 * (4 * factorial(3))
→ 5 * (4 * (3 * factorial(2)))
→ 5 * (4 * (3 * (2 * factorial(1))))
→ 5 * (4 * (3 * (2 * 1)))
→ 120
```

## When to Use Recursion
✅ Tree/graph traversal
✅ Factorial, Fibonacci
✅ Divide-and-conquer algorithms
❌ Simple loops (use for/while)
❌ Deep recursion (stack overflow)

## Recursion Depth Limit
```python
import sys
print(sys.getrecursionlimit())  # Usually 1000

# Increase limit if needed
sys.setrecursionlimit(10000)
```
