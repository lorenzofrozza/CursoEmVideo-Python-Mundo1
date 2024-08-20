import os 

# 13 CEV
os.system('cls')
wage_employee = float(input('Wage: U$'))
wage_increase = wage_employee + (wage_employee * 0.15) # or wage_employee * 15/100
print('  -The increase is 15% ')
print(f'\nWage with increase: U${wage_increase:.2f}')