# User Input and Typecasting

## What is User Input?

**User input** refers to data provided by the user through the keyboard or other input devices. In Python, the `input()` function is used to collect user input.

## The input() Function

```python
# Basic syntax
user_data = input("Enter your name: ")

# The input() function always returns a string
age = input("Enter your age: ")  # Returns string, not integer!
```

## User Input Examples

```python
# Getting user information
name = input("What is your name? ")
city = input("Which city do you live in? ")

# Display collected input
print(f"Hello {name}, from {city}!")
```

## What is Typecasting?

**Typecasting** (also called **type conversion**) is the process of converting data from one type to another. When you collect input using `input()`, it's always a string, so you need to convert it to the appropriate type.

## Type Conversion Functions

### Convert to Integer: int()

```python
age = input("Enter your age: ")      # "25" (string)
age = int(age)                       # 25 (integer)

# Direct conversion
age = int(input("Enter your age: "))
```

### Convert to Float: float()

```python
price = input("Enter price: ")       # "19.99" (string)
price = float(price)                 # 19.99 (float)

# Direct conversion
price = float(input("Enter price: "))
```

### Convert to String: str()

```python
age = 25                             # Integer
age_str = str(age)                   # "25" (string)

# Concatenation requires string
message = "I am " + str(age) + " years old"
```

### Convert to Boolean: bool()

```python
value = bool(input())                # True if non-empty
```

## Practical Examples

### Example 1: Order Calculation
```python
item = input("Item name: ")
quantity = int(input("Quantity: "))
price = float(input("Price per unit: "))

total = quantity * price
print(f"{quantity} x {item} = ${total:.2f}")
```

### Example 2: Age Verification
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Example 3: Grade Calculator
```python
name = input("Student name: ")
score = float(input("Exam score: "))
percentage = (score / 100) * 100

print(f"{name}'s score: {percentage}%")
```

## Common Type Conversion Errors

### Error 1: ValueError
```python
# Trying to convert non-numeric string to int
age = int("twenty-five")  # ValueError!

# Solution: Ensure input is numeric
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number")
```

### Error 2: TypeError
```python
# Trying to add string and integer
result = "5" + 10  # TypeError!

# Solution: Convert to same type
result = int("5") + 10  # 15
# OR
result = "5" + str(10)  # "510"
```

## Validation Techniques

### Check if String is Numeric
```python
user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    print(f"Number is {number}")
else:
    print("Invalid input")
```

### Try-Except for Type Conversion
```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")
```

### Range Validation
```python
age = int(input("Enter your age: "))
if 0 < age < 150:
    print("Valid age")
else:
    print("Age out of valid range")
```

## Multiple Inputs

```python
# Get multiple inputs
name, age = input("Enter name and age (comma-separated): ").split(',')
age = int(age.strip())

# Get inputs line by line
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
```

## Formatting Output with Converted Data

```python
# Using f-strings with converted types
price = float(input("Price: "))
quantity = int(input("Quantity: "))
total = price * quantity
print(f"Total: ${total:.2f}")

# Using format()
print("Total: ${:.2f}".format(total))

# Using %
print("Total: $%.2f" % total)
```

## Best Practices

✅ Always convert input to the appropriate type before using it  
✅ Validate user input before processing  
✅ Use try-except for error handling  
✅ Provide clear prompts to users  
✅ Give feedback on invalid input  
❌ Don't assume input is in the correct format  
❌ Don't perform calculations on string input  

## Exercises

1. Create a calculator that takes two numbers and an operator from user
2. Write a program to calculate BMI from height and weight input
3. Create a quiz where user answers are compared with correct answers
4. Make a program that validates user age (must be between 1-120)
5. Build a shopping cart that calculates total price with quantity conversion
