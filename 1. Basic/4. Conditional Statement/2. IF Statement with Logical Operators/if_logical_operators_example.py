"""
Conditional statement example with logical operators.
Determines door access based on age and membership.
"""

def can_enter_club(age, is_member):
    return age >= 18 and is_member

def main():
    age = 19
    is_member = False
    if can_enter_club(age, is_member):
        print("Access granted. Welcome to the club!")
    elif age >= 18 and not is_member:
        print("Membership required for entry.")
    else:
        print("Access denied. You must be at least 18 years old.")

if __name__ == "__main__":
    main()

# Exercises:
# 1. Add a special case to allow a guest pass if age >= 21 and not a member.
# 2. Change the code to check two boolean values: is_member or has_guest_pass.
# 3. Print a different message for members, guests, and underage visitors.
