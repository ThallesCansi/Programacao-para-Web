from os import system
system('clear')

number = int(input('Type a number: '))

if (number % 2 == 0):
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')