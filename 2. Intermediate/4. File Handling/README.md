# File Handling

## Reading Files

### Read Entire File
```python
with open("file.txt", "r") as file:
    content = file.read()
```

### Read Line by Line
```python
with open("file.txt", "r") as file:
    lines = file.readlines()

with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## Writing Files

### Write (Overwrites)
```python
with open("file.txt", "w") as file:
    file.write("Hello World")
```

### Append (Add to End)
```python
with open("file.txt", "a") as file:
    file.write("
New line")
```

## File Modes

- **r**: Read (default)
- **w**: Write (overwrites)
- **a**: Append (add to end)
- **x**: Create new file
- **r+**: Read and write

## Working with Different File Types

### CSV Files
```python
import csv

# Read CSV
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write CSV
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Ali", 25])
```

### JSON Files
```python
import json

# Read JSON
with open("data.json") as file:
    data = json.load(file)

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file)
```

## Best Practices

✅ Use with statement (auto-closes file)
✅ Handle FileNotFoundError
✅ Use appropriate mode
✅ Close files properly
