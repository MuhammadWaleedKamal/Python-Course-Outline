# Data Types

## What are Data Types?

A **data type** defines the type of value a variable can hold. Python determines the data type automatically when you assign a value, but you can also convert between types explicitly.

## Primary Data Types in Python

### 1. Integer (int)
Whole numbers without decimal points

```python
age = 25
temperature = -10
population = 1000000

# Operations
x = 10 + 5        # 15
y = 10 * 5        # 50
z = 10 // 3       # 3 (floor division)
w = 10 % 3        # 1 (modulo)
```

### 2. Float (float)
Numbers with decimal points

```python
price = 19.99
height = 1.75
pi = 3.14159

# Operations
total = 10.5 + 5.2      # 15.7
discount = 100 * 0.1    # 10.0
```

### 3. String (str)
Text data enclosed in quotes

```python
name = "Ahmed"
message = 'Hello World'
multiline = """This is
a multiline
string"""

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
repeated = "Hi" * 3                 # "HiHiHi"
```

### 4. Boolean (bool)
True or False values

```python
is_student = True
is_active = False

# Boolean operations
result = True and False      # False
result = True or False       # True
result = not True            # False
```

### 5. NoneType (None)
Represents absence of value

```python
value = None
result = None

# Checking for None
if value is None:
    print("Value is not set")
```

## Collection Data Types

### List
Ordered, mutable collection

```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Access elements
first = fruits[0]        # "apple"
last = fruits[-1]        # "orange"

# Modify elements
fruits[0] = "mango"
fruits.append("grape")
fruits.remove("banana")
```

### Tuple
Ordered, immutable collection

```python
coordinates = (10, 20)
rgb = (255, 128, 0)

# Access elements
x = coordinates[0]   # 10

# Tuples cannot be modified
# coordinates[0] = 5   # Error!
```

### Dictionary
Key-value pairs (unordered)

```python
student = {
    "name": "Ayesha",
    "age": 22,
    "gpa": 3.8
}

# Access values
name = student["name"]           # "Ayesha"
student["city"] = "Karachi"      # Add new key-value

# Check if key exists
if "age" in student:
    print(student["age"])
```

### Set
Unordered collection of unique items

```python
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4, 5}

# Add/remove items
colors.add("yellow")
colors.remove("red")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2       # {1, 2, 3, 4, 5}
intersection = set1 & set2 # {3}
```

## Type Conversion

```python
# String to Integer
age = int("25")              # 25
age = int(25.9)              # 25 (truncates)

# Integer to String
age_str = str(25)            # "25"

# String to Float
price = float("19.99")       # 19.99

# To Boolean
bool(0)                      # False
bool(1)                      # True
bool("")                     # False
bool("hello")                # True

# List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)    # (1, 2, 3)
```

## Type Checking

```python
# Check data type
type(25)                     # <class 'int'>
type("hello")                # <class 'str'>
type([1, 2, 3])              # <class 'list'>

# Using isinstance()
isinstance(25, int)          # True
isinstance("hello", str)     # True
isinstance([1, 2], list)     # True
```

## Common Type-Related Functions

```python
# Length
len("hello")                 # 5
len([1, 2, 3])              # 3

# Sum (for numbers)
sum([1, 2, 3, 4, 5])        # 15

# Min/Max
min([5, 2, 8, 1])           # 1
max([5, 2, 8, 1])           # 8

# Convert iterable to list
list("abc")                 # ['a', 'b', 'c']
list({1, 2, 3})             # [1, 2, 3] (order may vary)
```

## Exercises

1. Create variables with different data types and print their types
2. Convert string numbers to integers and perform arithmetic
3. Create a list of students with names, ages, and GPA
4. Write a program to check if a value exists in a set
5. Convert between different data types (list ↔ tuple, string ↔ int)
