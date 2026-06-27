# Nested IF Statement examples

number = 15
if number > 0:
    print("Number is positive")
    if number % 2 == 0:
        print("Number is also even")
    else:
        print("Number is odd")
else:
    print("Number is zero or negative")

age = 25
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can enter the club.")
    else:
        print("You can vote, but not enter the club.")
else:
    print("You are a minor.")

# ===== EXERCISE QUESTIONS =====
# 1. Check if a student has passed: score >= 40, then check if distinction (>= 75)
# 2. Check if login is valid (username exists), then check if password is correct
# 3. Check if a person is an adult (age >= 18), then check employment status
