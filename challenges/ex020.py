import os 
import random

# 20 CEV
os.system('cls')
student1 = input('Student 1: ')
student2 = input('Student 2: ')
student3 = input('Student 3: ')
student4 = input('Student 4: ')

list_students = [student1, student2, student3, student4]
random.shuffle(list_students)
print(f'\nThe order of presentation will be: ')
print("-"*3)
print(list_students)