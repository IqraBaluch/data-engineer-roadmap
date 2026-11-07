"""
Goal: print a receipt using f-strings.

Given:

item: "Notebook"
price: 250
quantity: 3
tax rate: 10%

Calculate:

subtotal = price × quantity
tax = subtotal × tax rate
total = subtotal + tax

Target output:

Item: Notebook
Price: 250
Qty: 3
Subtotal: 750
Tax: 75.00
Total: 825.00

"""
# variables and their values
item = "Notebook"
price = 250
quantity = 3
tax = 0.10

#calculations
subtotal = price * quantity
tax1 = subtotal * tax
total = subtotal + tax1

#displaying output using f-string
print(f"Item: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal}")
print(f"Tax: {tax1:.2f}")
print(f"Total: {total:.2f}")