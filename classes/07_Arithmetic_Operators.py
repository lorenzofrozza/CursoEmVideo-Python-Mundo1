# Arithmetic Operators
'''
 + addition, 5+5 = 10
 - subtraction, 5-2 = 3
 * multiplication, 5*3 = 18
 / division, 5/2 = 2,5
 // integer division, 5//2 = 2
 ** power of, 5**2 = 25
 %  module, rest of the division, 5%2 = 1
'''

# Order of precedence, PEMDAS
'''
1- Parentheses
2- Exponentiation
3- Multiplication, Division, Integer division, module
4- Addition, Subtraction
'''

# Practice

print(5+3*2)  # 11
print(5**2)  # 25
print(5**3)  # 125
print(19/2)  # 9.5
print(19//2)  # 9
print(18 % 2)  # 0
print(111 % 2)  # 1
print(4**3)  # 64
print(pow(4, 3))  # 64
print(81**(1/2))  # 9 square root
print(16**0.5)  # 4 square root
print(12**(1/3))  # cubic root

print('hi'+' hello')  # hi hello, concatenation
print('hi '*3)  # hi hi hi
print('='*15)  # ===============

# name = 'pedro' #input("What's your name? ") 
# print(f'Nice to meet you, {name}!') # Nice to meet you, pedro!
# print(f'Nice to meet you, {name:>20}!') # Nice to meet you,                pedro!
# print(f'Nice to meet you, {name:<20}!') # Nice to meet you, pedro               !
# print(f'Nice to meet you, {name:^20}!') # Nice to meet you,        pedro        !
# print(f'Nice to meet you, {name:-^20}!') # Nice to meet you, -------pedro--------!

number1 = int(input('Type a value: '))
number2 = int(input('Type another value: '))
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1/number2
integer_division = number1//number2
exponentiation = number1**number2
print('Addition: {}, Subtraction {}, Multiplication {}, Division {:.2f}'.format(addition,subtraction,multiplication,division), end=' ')
print('\nInteger division: {}, Exponentiation: {}'.format(integer_division,exponentiation))