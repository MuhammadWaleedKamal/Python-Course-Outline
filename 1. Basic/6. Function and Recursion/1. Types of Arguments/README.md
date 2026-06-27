# Types of Function Arguments

## Positional Arguments
Arguments passed in order

```python
def greet(name, age):
    print(f"{name} is {age}")

greet("Ali", 25)  # Positional
```

## Keyword Arguments
Arguments passed by name

```python
def greet(name, age):
    print(f"{name} is {age}")

greet(age=25, name="Ali")  # Keyword - order doesn't matter
```

## Default Arguments
Arguments with default values

```python
def greet(name, age=18):
    print(f"{name} is {age}")

greet("Ali")         # age uses default 18
greet("Sara", 20)    # age = 20
```

## Variable-Length Arguments (*args)
Accept any number of positional arguments

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_numbers(1, 2, 3, 4, 5)  # Returns 15
```

## Variable-Length Keyword Arguments (**kwargs)
Accept any number of keyword arguments

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Ali", age=25, city="Karachi")
```

## Combining All Types
```python
def func(pos, default=10, *args, **kwargs):
    pass
```
