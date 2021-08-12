"""
Write a program that will ask the user for his height (in cm) and body weight,
and as a result will present his BMI and recommendations.
Take a look at BMI definition in wikipedia.
"""

height_cm = int(input("what is your height in cm? "))
weight = float(input("what is your weight? "))

height_m = height_cm / 100

bmi = weight / height_m ** 2

print(f'You BMI is {bmi:.2f}')

if bmi < 18:
    print('You are underwieght')
elif 18 <= bmi <= 25:
    print('You have regular shape')
else:
    print('You are overweight')