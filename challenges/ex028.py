import os
import random
from time import sleep

os.system('cls')

shuffle_number = random.randint(0,5)
hunch = int(input('Guess the number (0 to 5): '))
print('Processing...')
sleep(2)

if hunch == shuffle_number: 
    print(f'\nCongratulations, you got the number right!!!')
else: 
    print('\nYou got the number wrong.')