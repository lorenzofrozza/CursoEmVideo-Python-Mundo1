import os 

# 12 CEV
os.system('cls')
product_price = float(input('Product price: U$'))
real_price = product_price - (product_price * 0.05)
print('  -The discount is 5%')
print(f'\nDiscount product price: U${real_price:.2f}')