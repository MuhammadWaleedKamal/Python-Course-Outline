# Generators and Iterators

## Iterators

Objects you can iterate over.

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
next(iterator)  # 1
next(iterator)  # 2
next(iterator)  # 3
# next(iterator)  # StopIteration
```

## Creating Iterators

```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

for num in Counter(3):
    print(num)  # 1, 2, 3
```

## Generators

Functions that yield values.

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up(3):
    print(num)  # 0, 1, 2
```

## Generator Expression

```python
squares = (x**2 for x in range(5))
print(list(squares))  # [0, 1, 4, 9, 16]
```

## Difference

- **Iterator**: Object with __iter__() and __next__()
- **Generator**: Function that yields values

## Benefits
✅ Memory efficient (lazy evaluation)
✅ Infinite sequences possible
✅ Simple syntax
