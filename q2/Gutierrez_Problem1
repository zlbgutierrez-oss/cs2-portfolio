# Calculates the total cost of the purchase.
def calculate_total(price, quantity):
    return price * quantity

# Calculates the change or the shortage if payment is insufficient.
def calculate_change(payment, total):
    return payment - total

# Ask the user for input.
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

# Pass price and quantity as arguments and store the returned total.
total = calculate_total(price, quantity)

# Reuse the stored total to calculate the change or shortage.
change = calculate_change(payment, total)

# Display the total cost and change or additional amount needed.
print(f"Total Cost: PHP {total:.2f}")

if change >= 0:
    print(f"Change: PHP {change:.2f}")
else:
    print(f"Additional amount needed: PHP {-change:.2f}")

# Documentation:
# 1. calculate_total() multiplies the price by the quantity.
#    calculate_change() subtracts the total from the payment.
# 2. Parameters (price, quantity) are variables in the function.
#    Arguments are the actual values passed when calling the function.
# 3. The returned total is stored in the variable 'total' and
#    reused in calculate_change() and the output.
# 4. Separate functions make the program easier to read,
#    understand, test, and maintain.
