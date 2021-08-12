"""
Interaction with the user and simple calculations (approx. 2 hours)
Ask user (using `input()` function) to provide the number of kilograms of
potatoes he'd like to buy and how much 1-kilogram costs.
The program should display how much user have to pay.
"""

quantity = float(input('How many kgs of potatoes do you need? '))
cost = float(input('How much 1-kg costs? '))

total_price = quantity * cost

print(f'The total price is {total_price} PLN')