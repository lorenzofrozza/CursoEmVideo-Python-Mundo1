import os
# Primitives Types 

# int = 5, 6, 87, 145
# float = 12.7, 0.123, 7.0
# bool = True, False
# str = 'Hello', '6.5'

# Data Output  
# print('Glad to meet you,',name,'!')
# print('Glad to meet you, {}!'.format(name))
# print(f'Glad to meet you, {name}!')

# Pratice
os.system('clear')

# number = input('Type a number: ')
# print(type(number))
# number = int(input('Type a value: '))
# number1 = int(input('Type another: '))
# addition = number + number1
# print('Result:',addition)
# print('The addition between {} and {} is: {}'.format(number,number1,addition))

x = input("Type something: ")
print(x.isnumeric()) # if x is a numeric it will returns True otherwise False
print(x.isalpha()) # if x is a alphabetical it will returns True otherwise False
print(x.isalnum()) # if x is a alphanumeric it will returns True otherwise False
print(x.isupper()) # if x there is only capital letters it will returns True otherwise False

