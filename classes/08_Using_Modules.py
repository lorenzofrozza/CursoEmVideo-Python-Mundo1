# The modules are to add features
'''
Import is used to import all features of a libraly
    EX: import drink
From is used to import a specific feature of a libraly and in this case u can just type the method whitout the prefix math
    EX: from dessert import cotton candy
'''

'''
import math
ceil - Round up
floor - Round down
trunc - eliminates everything from the comma forward
pow - power of
sqrt - square root
factorial - calculate factorial
'''
import math
import os

os.system('clear')
number = 5#int(input('Type a number: '))
square_root = math.sqrt(number)
print(f'\nSquare Root of {number} is {square_root}')
print(f'\nSquare Root of {number} is {math.ceil(square_root)}')
print(f'\nSquare Root of {number} is {math.floor(square_root)}')
print(f'\nSquare Root of {number} is {math.trunc(square_root)}')

from math import factorial
print(factorial(number))

import random 

num = random.random()
num1 = random.randint(1,10)
num2 = random.randrange(1,15)
print()
print(num)
print(num1)
print(num2)

import emojis

print(emojis.encode('Hello World :sunglasses:'))
