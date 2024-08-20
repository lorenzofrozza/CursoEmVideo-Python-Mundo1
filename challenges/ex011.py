import os 

# 11 CEV
os.system('cls')
wall_width = float(input("Type the width of the wall in meters: "))
wall_height = float(input("Type the height of the wall in meters: "))
wall_area = wall_width * wall_height
quantity_ink_liters = wall_area / 2
print(f'\nWall area: {wall_area} m2')
print(f'Quantity of paint needed: {quantity_ink_liters} liters')