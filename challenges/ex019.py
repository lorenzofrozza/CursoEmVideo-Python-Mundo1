import os 

# 19 CEV
os.system('cls')
import random
student1 = input('Student 1: ')
student2 = input('Student 2: ')
student3 = input('Student 3: ')
student4 = input('Student 4: ')

list_students = [student1, student2, student3, student4]
chosen = random.choice(list_students)
print(f'\nThe chosen student is {chosen}')