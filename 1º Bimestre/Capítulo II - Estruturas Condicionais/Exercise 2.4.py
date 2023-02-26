from os import system
system('clear')

year = int(input('Type a year: '))

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(f'The year {year} is leap year')
else:
    print(f'The year {year} is not leap year')