# BREAK and CONTINUE

## BREAK Statement
Exit loop immediately

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4
```

## CONTINUE Statement
Skip current iteration

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4 (skips 2)
```

## BREAK in WHILE
```python
count = 0
while True:
    print(count)
    count += 1
    if count > 5:
        break
```

## CONTINUE in WHILE
```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # Prints odd numbers
```

## BREAK with ELSE
```python
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed")  # Won't print (break was executed)
```

## Use Cases
- **break**: Exit when target found
- **continue**: Skip invalid items
- **else**: Cleanup after loop
