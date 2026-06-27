"""
File handling example.
Writes a shopping list to a file and reads it back.
"""

filename = "shopping_list.txt"
items = ["milk", "bread", "eggs"]

with open(filename, "w", encoding="utf-8") as file:
    for item in items:
        file.write(item + "
")

print(f"Saved {len(items)} items to {filename}.")

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print("Shopping list contents:")
print(content)

# Exercises:
# 1. Append a new item to the file instead of overwriting it.
# 2. Read the lines back into a list.
# 3. Count the number of items in the file.
