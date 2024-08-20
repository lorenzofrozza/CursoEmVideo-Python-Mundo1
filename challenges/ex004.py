# 04 CEV
import os

os.system('cls')
y = input('Type something: ')
print('Primitive Type:',type(y))
print(f'Numeric: {y.isnumeric()}')
print(f'Alphabetical: {y.isalpha()}')
print(f'Alphanumeric: {y.isalnum()}')
print(f'Only capital letters: {y.isupper()}')
print(f'Only low case letters: {y.islower()}')
print(f'Is it captalize: {y.istitle()}')
print(f'Only spaces: {y.isspace()}')