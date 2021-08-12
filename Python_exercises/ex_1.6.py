"""
Assumptions:
    - 0-6   - kindergarten - ticket price: 0
    - 7-17  - school       - ticket price: 2.28
    - 18-64 - adult        - ticket price: 3.80
    - +65   - pensioner    - ticket price: 1.90
Write a program that will ask a user for his age and a number of tickets he'd like to buy.
Based on the assumptions above calculate the price he should pay for the tickets.
"""

age = int(input('What is your age? '))
tickets = int(input('How many tickets would you like? '))

if age <= 6:
    print('For children under 6 years entrance is for free')
elif 6 < age <= 17:
    print(f'Total price for {tickets} student tickets is {2.28 * tickets:.2f} PLN')
elif 17 < age <= 64:
    print(f'Total price for {tickets} adult tickets is {3.80 * tickets:.2f} PLN')
elif age > 64:
    print(f'Total price for {tickets} senior tickets is {1.90 * tickets:.2f} PLN')




