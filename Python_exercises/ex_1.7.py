"""
Ask a user for a product he'd like to byt, its quantity and price. Based on that display a proper information.
Example:
What would you like to buy? - tomatoes
Provide a price - 5
Provide quantity - 10
For tomatoes, you'd like to buy, you have to pay 50 PLN.
"""

product = input('What would you like to buy sir? ')
quantity = int(input("How many? "))
price = float(input('How much is the price for one? '))

print(f'For {quantity} {product} you will have to pay {quantity * price:.2f} PLN')