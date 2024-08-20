import os 
from datetime import date

os.system('cls')
year = int(input('Type a year to see if it is a leap year? Type 0 to analyze the current year: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year %400 ==0:
    print(f'\nYear: - {year} -\nIt is a leap year!!')
else:
    print(f'\nYear: - {year} -\nIt is not a leap year!!')
 
#ano = int(input())

# if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#     print('Ano bissexto.')
# else:
#     print('Não é um ano bissexto.')