import os 

# 18 CEV
os.system('cls')
import math
angle = float(input('Enter the angle that you want: '))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print(f'\nThe angle of {angle} degrees has the sine of {sine:.2f} degrees')
print(f'The angle of {angle} degrees has the cosine of {cosine:.2f} degrees')
print(f'The angle of {angle} degrees has the tangent of {tangent:.2f} degrees')