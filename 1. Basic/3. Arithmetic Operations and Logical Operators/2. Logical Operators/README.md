# Logical Operators

## What are Logical Operators?

**Logical operators** are used to combine conditional statements and create complex boolean expressions. They return True or False based on the conditions they evaluate.

## Three Main Logical Operators

### 1. AND (and)
Returns True if BOTH conditions are True

```python
age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("Can drive")  # This prints
```

**Truth Table for AND:**
| A | B | A and B |
|---|---|---------|
| T | T | T       |
| T | F | F       |
| F | T | F       |
| F | F | F       |

### 2. OR (or)
Returns True if AT LEAST ONE condition is True

```python
day = "Saturday"
is_holiday = False

# At least one must be True
if day == "Saturday" or is_holiday:
    print("No work today")  # This prints
```

**Truth Table for OR:**
| A | B | A or B |
|---|---|--------|
| T | T | T      |
| T | F | T      |
| F | T | T      |
| F | F | F      |

### 3. NOT (not)
Reverses the boolean value

```python
is_raining = False

# NOT reverses the value
if not is_raining:
    print("Go outside")  # This prints
```

**Truth Table for NOT:**
| A | not A |
|---|-------|
| T | F     |
| F | T     |

## Combining Logical Operators

```python
# Multiple conditions
age = 22
salary = 45000
has_good_credit = True

if age >= 21 and salary >= 30000 and has_good_credit:
    print("Eligible for loan")

# Using OR with multiple conditions
if age < 13 or age > 65:
    print("Special rate available")

# Mixing AND, OR, NOT
if (age >= 18 and has_license) or is_supervised:
    print("Can drive")
```

## Operator Precedence

When combining logical operators, they are evaluated in this order:

1. **NOT** (highest priority)
2. **AND**
3. **OR** (lowest priority)

```python
# Order matters!
True or False and False      # True (AND evaluated first)
(True or False) and False    # False (parentheses first)

not True and False           # False (NOT first, then AND)
not (True and False)         # True (parentheses first)
```

## Short-Circuit Evaluation

Python stops evaluating as soon as it knows the answer:

```python
# With AND: stops at first False
False and expensive_function()  # Function not called!

# With OR: stops at first True
True or expensive_function()    # Function not called!
```

## Practical Examples

### Example 1: Login Validation
```python
username = "ayesha"
password = "secure123"
is_verified = True

if username == "ayesha" and password == "secure123" and is_verified:
    print("Login successful")
else:
    print("Login failed")
```

### Example 2: Eligibility Check
```python
age = 25
income = 50000
credit_score = 750

# Must be 21+ with income 30000+ and credit 700+
if age >= 21 and income >= 30000 and credit_score >= 700:
    print("Eligible for credit card")
else:
    print("Not eligible")
```

### Example 3: Discount Eligibility
```python
is_member = True
purchase_amount = 150
is_holiday = False

# Get discount if member OR purchase > 100 OR on holiday
if is_member or purchase_amount > 100 or is_holiday:
    print("10% discount applied")
else:
    print("No discount")
```

### Example 4: Activity Recommendation
```python
temperature = 28
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Perfect time to go outdoors!")
else:
    print("Stay indoors")
```

## Common Logical Patterns

### Both Conditions Must Be True
```python
if password_correct and username_exists:
    print("Login successful")
```

### Either Condition Can Be True
```python
if user_is_admin or user_is_moderator:
    print("Access granted")
```

### Condition Must NOT Be True
```python
if not is_banned:
    print("Welcome!")
```

### Nested Logic
```python
if age >= 18:
    if has_license:
        if not is_suspended:
            print("Can drive")
```

## Converting to Logical Operators

### Multiple If Statements
```python
# Without logical operators
if age >= 18:
    if has_license:
        print("Can drive")

# With logical operators (better)
if age >= 18 and has_license:
    print("Can drive")
```

### Avoiding Double Negatives
```python
# Hard to read
if not age < 18:
    print("Adult")

# Better (clearer intent)
if age >= 18:
    print("Adult")
```

## Truthiness in Python

Any value can be evaluated as True or False:

```python
# Falsy values
bool(0)           # False
bool("")          # False
bool([])          # False
bool(None)        # False
bool(False)       # False

# Truthy values
bool(1)           # True
bool("hello")     # True
bool([1, 2])      # True
bool(True)        # True
```

## Exercises

1. Write a program to check if a student is eligible to graduate (GPA ≥ 3.0 AND completed all courses)
2. Create a discount calculator that applies discount if member OR purchase > $100 OR on holiday
3. Validate password strength (length ≥ 8 AND has uppercase AND has numbers)
4. Check if person can rent a car (age ≥ 21 AND has license AND not blacklisted)
5. Determine if attendance is good (attendance > 80% AND no failing grades OR special circumstances)
