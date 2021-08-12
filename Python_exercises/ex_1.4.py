"""
Write a program, where the user provides his age and the number of nights he wants to stay at the hotel.
Based on that values calculate the fee for his stay. The rules are:
- minor (below 18 years old) will pay 100 PLN per night
- adults (of age 18 but less than 65) will pay:
    - 200 PLN if they are staying for one night
    - 180 PLN if they are staying for at least 2 nights but less than 5
    - 150 PLN if they are staying for 5 and more nights
- pensioners (65 and older) will pay the same rate as adults but with a 10% discount
For example, if a user is 70 years old and will spend 10 nights at the hotel,
he will pay 150 PLN - 10% discount = 135 PLN per night, so for the whole stay, he will pay 1350 PLN.
"""

age = int(input('What is your age? '))
nights = int(input('How many nights will you stay? '))

price_1 = 180 * nights
price_2 = 150 * nights


if age < 18:
    print(f"the price for you is {100 * nights} PLN")
elif 18 <= age < 65:
    if nights == 1:
        print('Your total price is 200 PLN')
    elif 2 <= nights < 5:
        print(f'Your total price is {price_1} PLN')
    elif nights >= 5:
        print(f'Your total price is {price_2} PLN')
elif age >= 65:
    if nights == 1:
        print(f'Your total price is {200 * 0.9} PLN')
    elif 2 <= nights < 5:
        print(f'Your total price is {price_1 * 0.9} PLN')
    elif nights >= 5:
        print(f'Your total price is {price_2 * 0.9} PLN')