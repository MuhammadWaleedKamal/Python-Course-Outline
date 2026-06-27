"""
For loop example.
Computes weekly average sales from a list of daily sales.
"""

def average_sales(daily_sales):
    total = 0
    for sale in daily_sales:
        total += sale
    return total / len(daily_sales)

def main():
    daily_sales = [120.00, 150.50, 99.99, 180.00, 210.25]
    average = average_sales(daily_sales)
    print("Daily sales:", daily_sales)
    print(f"Average sales for the week: ${average:.2f}")

if __name__ == "__main__":
    main()

# Exercises:
# 1. Update the script to include weekend sales and compute a 7-day average.
# 2. Use a for loop to count how many days exceeded $150 in sales.
# 3. Print a warning if the average sales are below $120.
