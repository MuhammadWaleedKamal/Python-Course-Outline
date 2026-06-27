"""
Logical operators example.
Checks whether a customer is eligible for a loan.
"""

def is_loan_eligible(age, salary, has_good_credit):
    return age >= 21 and salary >= 30000 and has_good_credit

def main():
    age = 28
    salary = 42000
    has_good_credit = True
    eligible = is_loan_eligible(age, salary, has_good_credit)
    print("Loan eligibility check:")
    print(f"Age: {age}, Salary: ${salary}, Good credit: {has_good_credit}")
    print("Eligible for loan:", "Yes" if eligible else "No")

if __name__ == "__main__":
    main()

# Exercises:
# 1. Add a second loan type with a different salary requirement and print which loans the customer qualifies for.
# 2. Use or / not to check whether a customer is ineligible due to low salary or bad credit.
# 3. Allow the user to enter age, salary, and credit status at runtime.
