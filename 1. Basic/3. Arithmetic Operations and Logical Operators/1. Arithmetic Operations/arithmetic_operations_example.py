"""
Arithmetic operations example.
Calculates a shopping bill with tax and discount.
"""

def calculate_total(price, quantity, tax_rate, discount_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    discount = subtotal * discount_rate
    total = subtotal + tax - discount
    return subtotal, tax, discount, total

def main():
    price = 12.50
    quantity = 4
    tax_rate = 0.07
    discount_rate = 0.10
    subtotal, tax, discount, total = calculate_total(price, quantity, tax_rate, discount_rate)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Total amount due: ${total:.2f}")

if __name__ == "__main__":
    main()

# Exercises:
# 1. Change the program so it asks the user for price, quantity, tax rate, and discount rate.
# 2. Add a delivery fee and include it in the final total.
# 3. Display a message if the order total is above $50.
