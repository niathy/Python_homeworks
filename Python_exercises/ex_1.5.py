"""
Write a program that will ask a user for the lengths of the sides of a triangle.
Check if it's possible to create a triangle from those lengths and if so, calculate the area of the triangle.
To calucate squre root use:
```
import math
x = math.sqrt(10)
```
"""

from math import sqrt

x = float(input("side 1: "))
y = float(input('side 2: '))
z = float(input('side 3: '))


if x < (y + z) and y < (x + z) and z < (x +y):
    print('It is possible to calculate the area')

    p = (x + y + z) / 2
    a = sqrt(p * (p - x) * (p - y) * (p - z))
    print(f'The are of the triangle is {a:.2f} cm2')

else:
    print('You can\'t have a triagle from these sides')



