# Variables

## What are Variables?

A **variable** is a named container that stores a value in memory. Think of it as a labeled box where you can put data and retrieve it later by using its name.

## Variable Naming Rules in Python

Variables must follow these rules:
- Start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, digits (0-9), and underscores
- Cannot contain spaces
- Cannot use Python keywords (if, for, class, etc.)
- Are case-sensitive (name ≠ Name ≠ NAME)

## Naming Conventions

### Valid Variable Names
```python
age = 25
user_name = "Ayesha"
_private = 100
name2 = "John"
```

### Invalid Variable Names
```python
2age = 25          # Starts with number
user-name = "Ali"  # Contains hyphen
for = 10           # Python keyword
user name = "Sara" # Contains space
```

## Variable Assignment

```python
# Single assignment
x = 10

# Multiple assignment
a, b, c = 1, 2, 3

# Unpacking
values = [10, 20, 30]
x, y, z = values

# Swap values
a, b = b, a
```

## Variable Scope

### Local Scope
Variables defined inside a function are local to that function

```python
def greet():
    name = "Ali"  # Local variable
    print(name)

greet()           # Works
print(name)       # Error: name not defined
```

### Global Scope
Variables defined at module level are accessible everywhere

```python
name = "Global"   # Global variable

def greet():
    print(name)   # Accessible here

greet()           # Prints "Global"
```

## Variable Types and Memory

```python
# Different data types
age = 25          # Integer
price = 19.99     # Float
name = "Ahmed"    # String
is_active = True  # Boolean
```

## Common Variable Operations

```python
# Reassignment
score = 100
score = 95

# Increment/Decrement
count = 5
count += 1        # count = 6
count -= 2        # count = 4

# Type checking
type(age)         # <class 'int'>
isinstance(age, int)  # True
```

## Best Practices

✅ Use meaningful variable names  
✅ Use snake_case for variable names  
✅ Declare variables close to where they're used  
✅ Initialize variables before using them  
✅ Use constants for fixed values (in UPPERCASE)  
❌ Don't use single letters (except i, j for loops)  
❌ Don't use ambiguous names like "x", "data", "temp"  

## Exercises

1. Create variables to store: your name, age, city, and whether you're a student
2. Write a program to calculate total cost: quantity × price per unit
3. Swap two variables without using a third variable
4. Create a program showing variable scope (local and global)
5. Demonstrate type checking with isinstance()
