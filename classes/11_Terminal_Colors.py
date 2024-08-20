# Theoretical part
'''
Always that u want to represent a color in pyhton we will initialize with:
\003[style;text;backm
\003[0;33;44m #example

codes to style: 0 nothing
                1 bold 
                4 underline
                7 neagtivete

text colors:    30 white
                31 red
                32 green
                33 yellow
                34 blue
                35 magenta (like purple)
                36 cyan
                37 grey
                # but u can put more

back colors:    40 white
                41 red
                42 green
                43 yellow
                44 blue
                45 magenta
                46 cyan
                47 grey
'''

# Pratical part
# from time import sleep

# print('\033[1;31;43mHello world!\033[m')
# sleep(1)
# print('\033[34mHello world!\033[m')
# sleep(1)
# print('\033[7;31mHello world!\033[m')
# sleep(1)
# print('\033[0;33;44mHello world!\033[m')
# sleep(1)
# print('\033[7;33;44mHello world!\033[m')

a = 5
b = 7

colors = {'clean': '\033[m',    # u can create a list of colors
          'blue':'\033[34m',
          'yellow':'\033[33m',
          'blackandwhite': '\033[7;30m'}

print(f'The values are \033[0;33;45m{a} and {b}\033[m')
print(f'The values are \033[0;33;45m{a}\033[m and {b}')
print(f'The values are {a} \033[0;33;45mand\033[m {b}')
print(f'The values are {a} and \033[0;33;45m{b}\033[m')
print(f'The values are \033[4;34m{a} \033[0;33;45mand\033[m {b}\033[m')

name = 'Lorenzo'
print('Glad to meet you, {}{}{}!!'.format(colors['yellow'], name, colors['clean']))
print('Glad to meet you, {}{}{}!!'.format(colors['blackandwhite'], name, colors['clean']))
