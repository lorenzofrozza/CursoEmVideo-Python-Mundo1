import os 

os.system('cls')
number = int(input('Type a number to see if is even or odd: '))

if number % 2 == 0:
    print(f'\n- {number} -\nEVEN!')
else:
    print(f'\n- {number} -\nODD!')