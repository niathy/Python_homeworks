"""
Lets assume that 1 dog year equals 5 human years.
Ask a user what is the name of his dog and how old is he and calculate dogs age, if he would be a human.
Example:
Provide name of the dog - Lassie
Provide dogs age - 3
If Lassie was a human, would have 15 years.
"""

name = input('What is the name of your dog? ')
age = int(input('How old is it? '))

human_age = age * 5

print(f'If {name} was a human it would be {human_age} yesars old')