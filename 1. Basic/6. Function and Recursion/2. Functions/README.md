# Functions

## What is a Function?

Reusable block of code that performs a specific task.

## Function Definition
```python
def function_name(parameters):
    """Function description"""
    # Code
    return result
```

## Function Components

1. **def**: Define function
2. **name**: Function identifier
3. **parameters**: Input variables
4. **docstring**: Description
5. **body**: Code to execute
6. **return**: Output value

## Calling Functions
```python
result = function_name(arguments)
```

## Return Values
```python
def add(a, b):
    return a + b

result = add(5, 3)  # 8
```

## Multiple Return Values
```python
def get_info():
    return "Ali", 25, "Karachi"

name, age, city = get_info()
```

## Scope

**Local**: Inside function
**Global**: Outside function

```python
global_var = 10

def func():
    local_var = 5  # Only in func()
    return global_var + local_var

func()  # 15
print(local_var)  # Error: local_var not defined
```

## Best Practices
✅ Clear, descriptive names
✅ Single responsibility
✅ Use docstrings
✅ Keep functions small
❌ Too many parameters
