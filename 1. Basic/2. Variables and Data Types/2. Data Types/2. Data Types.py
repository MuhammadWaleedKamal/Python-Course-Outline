"""
Data types example.
Uses strings, integers, floats, lists, and booleans in a payroll scenario.
"""

employee_name = "Ayesha"
age = 30
salary = 45000.50
is_full_time = True
benefits = ["Health insurance", "Transport allowance", "Paid leave"]

print("Employee:", employee_name)
print("Age:", age)
print(f"Salary: ${salary:.2f}")
print("Full-time employee:", is_full_time)
print("Benefits:")
for benefit in benefits:
    print("-", benefit)

# Exercises:
# 1. Convert salary to an integer and print the result.
# 2. Change is_full_time to False and print a notice if the employee is part-time.
# 3. Add a new benefit to the list and print the updated benefits.
