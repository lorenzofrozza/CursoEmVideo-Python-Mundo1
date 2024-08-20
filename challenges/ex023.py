import os 
os.system('cls')
number = int(input('Type a number between 0 to 9999: '))
u = number // 1 %10
d = number // 10 %10
c = number // 100 %10
m = number // 1000 %10

print(f'\n-- {number} --\n')
print(f'Unit: {u}')
print(f'Ten: {d}')
print(f'Hundreds: {c}')
print(f'Thousands: {m}')