import os 

# 08 CEV
os.system('cls')
table_meters = float(input("Type your table's width in meters: "))
table_centimeters = table_meters * 100
table_millimeters = table_meters * 1000
print(f'- Measuring Table -\n\nMeters: {table_meters}\nCentimeters: {table_centimeters}\nMillimeters: {table_millimeters}')