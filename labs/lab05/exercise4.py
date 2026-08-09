# Takes item name and price from the user
item_name = input("Enter the item name:")
item_price = float(input("Enter the item price:"))

# Creates variables for quantity (3 items) and tax rate (6%)
quantity = 3
tax_rate = 0.06

# Calculates and displays subtotal, tax amount, and total cost
subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print(f"Item Name: {item_name}")
print(f"Item Price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print