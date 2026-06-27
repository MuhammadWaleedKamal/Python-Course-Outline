# Lambda Functions

## What are Lambda Functions?

Anonymous functions for simple operations.

## Syntax
```python
lambda arguments: expression
```

## Examples

```python
# Simple lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda with conditional
get_age_category = lambda age: "Adult" if age >= 18 else "Minor"
```

## Using with map()
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16]
```

## Using with filter()
```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
```

## Using with sorted()
```python
students = [("Ali", 22), ("Sara", 20), ("Ayesha", 23)]
sorted_by_age = sorted(students, key=lambda x: x[1])
```

## When to Use

✅ Simple one-expression functions
✅ With map(), filter(), sorted()
✅ As callback functions

❌ Complex logic
❌ Multiple statements
❌ When you need to reuse the function

## Readability
```python
# Hard to read
process = lambda x: sum([i for i in range(x) if i % 2 == 0])

# Better to use regular function
def sum_even_up_to(x):
    return sum([i for i in range(x) if i % 2 == 0])
```
