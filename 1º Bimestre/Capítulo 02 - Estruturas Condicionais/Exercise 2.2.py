from os import system
system('clear')

number = int(input('Type a number: '))

if (number > 0):
    print(f'{number} is positive number')
elif (number < 0):
    print(f'{number} is negative numbebr')
else:
    print(f'You type zero ({number}) number.')