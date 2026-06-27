"""
Main guard example.
Shows how code runs only when the script is executed directly.
"""

def display_message():
    print("This script is running directly, not imported.")

if __name__ == "__main__":
    display_message()

# Exercises:
# 1. Add another function and call it from the main guard.
# 2. Import this script from another file and check __name__.
# 3. Print a message before and after the main guard.
