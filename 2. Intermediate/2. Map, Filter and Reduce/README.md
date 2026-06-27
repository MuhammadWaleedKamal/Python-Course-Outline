# Map, Filter, and Reduce

## MAP Function

Apply function to all items in iterable.

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
```

## FILTER Function

Keep only items matching condition.

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
```

## REDUCE Function

Combine all items into single value.

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
# 15
```

## Using with Functions

```python
def double(x):
    return x * 2

numbers = [1, 2, 3]
result = list(map(double, numbers))  # [2, 4, 6]
```

## Combining Operations

```python
from functools import reduce

prices = [100, 200, 150, 75]
# Apply 10% discount
discounted = map(lambda p: p * 0.9, prices)
# Filter >= 100
expensive = filter(lambda p: p >= 100, discounted)
# Sum total
total = reduce(lambda x, y: x + y, expensive)
```

## Alternatives (Often Clearer)

```python
# Instead of map
squared = [x**2 for x in numbers]

# Instead of filter
evens = [x for x in numbers if x % 2 == 0]

# Instead of reduce
total = sum(numbers)
```
