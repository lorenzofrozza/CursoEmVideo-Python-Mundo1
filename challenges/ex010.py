import os 

# 10 CEV
os.system('cls')
wallet = float(input('How many reais do you have in your wallet? R$'))
dollar = 3.27
buy_dollar = wallet / dollar
print(f'You can buy: U${buy_dollar:.2f}')