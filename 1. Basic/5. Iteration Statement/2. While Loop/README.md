# WHILE Loops

## Basic WHILE Loop
```python
while condition:
    # Execute while condition is True
    # Must change condition to avoid infinite loop
```

## Counting Example
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## User Input Loop
```python
while True:
    user_input = input("Enter (q to quit): ")
    if user_input == "q":
        break
    print(f"You entered: {user_input}")
```

## WHILE with ELSE
```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed")
```

## Best Practices
✅ Always update the condition variable
✅ Avoid infinite loops
✅ Use break to exit early
✅ Use continue to skip iteration
❌ Don't forget to change loop variable
