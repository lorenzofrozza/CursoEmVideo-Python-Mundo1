import os 

os.system('cls')
number1 = float(input('First number: '))
number2 = float(input('Second number: '))
number3 = float(input('Third number: '))

#Checking the lowest number 
lowest = number1
if number2 < number1 and number2 < number3:
    lowest = number2
if number3 < number1 and number3 < number2:
    lowest = number3

#Checking the highest number 
highest = number1
if number2 > number1 and number2 > number3:
    highest = number2
if number3> number1 and number3 > number2:
    highest = number3

print(f'\nThe highest number is - {highest} -')
print(f'The lowest number is - {lowest} -')