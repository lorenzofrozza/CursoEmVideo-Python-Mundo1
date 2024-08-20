import os 

os.system('cls')

line1 = float(input('Type the length of the first line: '))
line2 = float(input('Type the length of the second line: ')) 
line3 = float(input('Type the length of the third line: '))

h1 = line1 + line2
h2 = line2 + line3
h3 = line1 + line3
if h1 > line3 and h2 > line1 and h3 > line2:
    print('\nThe lines CAN form a triangle.')
else:
    print('\nThe lines CANNOT form a triangle.')