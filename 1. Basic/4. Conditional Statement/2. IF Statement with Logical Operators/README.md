# IF Statements with Logical Operators

## Combining Conditions with AND
```python
if age >= 18 and has_license:
    print("Can drive")
```

## Combining Conditions with OR
```python
if is_weekend or is_holiday:
    print("No work")
```

## Using NOT
```python
if not is_raining:
    print("Go out")
```

## Complex Logic
```python
if (age >= 18 and has_license) or is_supervised:
    print("Permission granted")
```

## Best Practices
✅ Keep conditions simple and readable
✅ Use parentheses for clarity
✅ Avoid double negatives
❌ Don't nest too deeply
