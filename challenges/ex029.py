import os

os.system('cls')
speed = float(input('Type the speed the your car passed the radar: '))
speed_limit = 80
fine = (speed - speed_limit) * 7

if speed > 80:
    print(f'\n- Speed: {speed}-\nYou were fined!\nValue of fine: {fine} ')
else:
    print(f'\n- Speed: {speed}- \nYou were not fined')
