import os

os.system('cls')
employee_wage = float(input('What is your wage: '))

if employee_wage > 1250:
    increase_wage = employee_wage + (employee_wage * 0.1) # or employee_wage * 10/100
    print(f'\nYour old wage is: U${employee_wage}')
    print(f'Your wage with increase is: U${increase_wage}')
else:
    increase_wage = employee_wage + (employee_wage * 0.15) # or employee_wage * 15/100
    print(f'\nYour old wage is: U${employee_wage}')
    print(f'Your wage with increase is: U${increase_wage}')
