# Exception Handling

## What are Exceptions?

Errors during program execution.

## Try-Except

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Enter a valid number")
```

## Multiple Exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value")
except Exception:
    print("Unexpected error")
```

## Try-Except-Finally

Always executes.

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
```

## Try-Except-Else

Runs if no exception.

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"Number is {number}")
```

## Raising Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

## Common Exceptions

- **ValueError**: Invalid value
- **TypeError**: Wrong type
- **ZeroDivisionError**: Divide by zero
- **FileNotFoundError**: File doesn't exist
- **IndexError**: Index out of range
- **KeyError**: Dictionary key missing
- **AttributeError**: Attribute doesn't exist

## Best Practices

✅ Catch specific exceptions
✅ Use finally for cleanup
✅ Provide helpful error messages
❌ Catch all exceptions (bare except)
❌ Ignore errors silently
