full_name = str(input('Type your full name: '))

print(f'\n{full_name.upper()}') #01

print(full_name.lower()) #02 

counter = full_name.replace(' ', '') #03
print(len(counter))

slice = full_name.split() #04
print(len(slice [0]))