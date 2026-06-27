# FOR Loops

## Iterating Over Range
```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

## Iterating Over List
```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

## Iterating Over String
```python
for char in "hello":
    print(char)
```

## Using range() with Start, Stop, Step
```python
range(5)        # 0 to 4
range(1, 5)     # 1 to 4
range(0, 10, 2) # 0, 2, 4, 6, 8
```

## Loop with Index
```python
for i, fruit in enumerate(["apple", "banana"]):
    print(f"{i}: {fruit}")
```

## Loop with Dictionary
```python
student = {"name": "Ali", "age": 22}
for key, value in student.items():
    print(f"{key}: {value}")
```

## Loop Control
- **break**: Exit loop
- **continue**: Skip iteration
- **else**: After loop completes
