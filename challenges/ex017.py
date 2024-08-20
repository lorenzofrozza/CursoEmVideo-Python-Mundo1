import os

# 17 CEV
os.system('cls')
from math import pow
from math import sqrt
from math import hypot
adjacent_catheter = float(input('Type de length of the adjacent catheter: '))
opposite_catheter = float(input('Type de length of the opposite catheter: '))
h = sqrt(((pow(adjacent_catheter,2)) + (pow(opposite_catheter,2))))
hm = hypot(adjacent_catheter, opposite_catheter)
print(f'\nThe value of the hypotenuse is -{h:.2f}-')
print(f'\nThe value of the hypotenuse is -{hm:.2f}-')