"""
Assumptions:
    - 0-6   - kindergarten - ticket price: 0
    - 7-17  - school       - ticket price: 2.28
    - 18-64 - adult        - ticket price: 3.80
    - +65   - pensioner    - ticket price: 1.90
Write a program that will ask a user for his age and a number of tickets he'd like to buy.
Based on the assumptions above calculate the price he should pay for the tickets.
"""

children = int(input('How many children under 7 years? '))
students = int(input('How many students from 7 to 17 years? '))
adults = int(input('How many adults from 18 to 64 years? '))
seniors = int(input('How many seniors older than 65? '))

price = (2.28 * students) + (3.80 * adults) + (1.90 * seniors)

if children != 0 and students == 0 and adults == 0 and seniors == 0:
    print("Entrance for children below 7 years old is for free")
else:
    print(f'The total price for your group is {price} PLN')


