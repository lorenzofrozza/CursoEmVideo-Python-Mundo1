import os 

# 14 CEV
os.system('cls')
degrees_celsius = float(input('Inform the temperature in C: '))
formula_fahrenheit =  (degrees_celsius * 9/5) + 32
print(f'\nThe temperature of {degrees_celsius}C corresponds to {formula_fahrenheit}F')
