import os
#Simple, compound and simplified conditions

# name = str(input('Type your name: '))

# if name == ('Gustavo'):
#     print('What a beautiful name you have!')
# else:
#     print('Your name is so normal!')
# print(f'\nGood Morning, {name}!')

os.system('cls')
grade_1 = float(input('Type the first grade: '))
grade_2 = float(input('Type the second grade: '))

average = (grade_1 + grade_2) / 2
# print(f'\nCongratulations' if average>=6 else '\nStudy more') #Other way to write

if average >=6:
    print(f'\nYour average was {average:.2f}')
    print(f'You are APPROVED!')
else:
    print(f'\nYour average was {average:.2f}')
    print(f'You are DISAPPROVED!')


