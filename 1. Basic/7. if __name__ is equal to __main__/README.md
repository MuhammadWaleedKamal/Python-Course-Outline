# if __name__ == "__main__"

## What is __name__?

Special variable that tells you how Python executed the script.

## Values of __name__

When **executing directly**:
```python
__name__ == "__main__"
```

When **importing as module**:
```python
__name__ == "module_name"
```

## Usage Pattern

```python
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Ali")
```

## Why Use It?

1. **Test code**: Run tests only when script is main
2. **Dual purpose**: Use as module or standalone
3. **Prevent auto-execution**: Don't run when imported

## Example

**script.py**
```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(5, 3)
    print(result)
```

**When run directly**: Script executes
**When imported**: Function available, but script doesn't run

## Best Practices

✅ Always use for executable code
✅ Keep main code separate
✅ Makes code more reusable
❌ Don't put all code in main block
