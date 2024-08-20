import os 

# 15 CEV
os.system('cls')
kilometeres_treveled = float(input('How many kilometers did you drive with the rental car? '))
quantity_days_car_rental = float(input('How many days did you rent the car? '))
value_pay = (quantity_days_car_rental * 60) + (kilometeres_treveled * 0.15)
print(f'Total to pay: U${value_pay:.2f}')