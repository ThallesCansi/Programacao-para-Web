from os import system
system('clear')

age = int(input('How old are you? '))

if (age > 18):
    print('You are of legal age')
else:
    print("You're not yet legal age")