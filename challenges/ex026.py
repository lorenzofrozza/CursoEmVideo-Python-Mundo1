import os
os.system('cls')
sentence = str(input('Type a sentence: ')).lower().strip()

letter_a = sentence.count('a') #01
print(f'\nThe letter -A- appears {letter_a} times in the sentence.')
find_first_a = sentence.find('a') + 1 #02
print(f'The first letter -A- appeared in the {find_first_a} position.')
find_last_a = sentence.rfind('a') + 1
print(f'The last letter -A- appeared in the {find_last_a} position.')