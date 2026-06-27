"""
While loop example.
Simulates a login attempt counter for a website.
"""

attempts_left = 3
correct_password = "python123"

while attempts_left > 0:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Login successful. Welcome!")
        break
    attempts_left -= 1
    print(f"Incorrect password. Attempts left: {attempts_left}")
else:
    print("Account locked. Please try again later.")

# Exercises:
# 1. Allow five login attempts instead of three.
# 2. Print the username after a successful login.
# 3. Track and print the number of failed attempts.
