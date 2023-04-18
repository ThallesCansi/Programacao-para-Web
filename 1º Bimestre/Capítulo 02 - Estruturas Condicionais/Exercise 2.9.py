stripString = list()

month = list()
day = list()

string = input('Enter a date in mm/dd/yyyy format: ')

for i in range(1, 32):
    if (i <= 12):
        month.append(i)
    day.append(i)

splitString = string.split('/')
splitString = [int(i) for i in splitString]

year = splitString[2]

if (string[2] == '/' or string[1] == '/' and string[5] == '/' or string[4] == '/' and len(string) < 10):
    if ((splitString[0] in month) and (splitString[1] in day)):
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            if (splitString[0] == 2 and splitString[1] <= 29):
                print(f'The string have correctly format: {string}')
            else:
                print(f'The year {year} is not leap year and have correctly format: {string}')
    else:
        print('Please, enter the correctly format for month and days.')
else:
    print('Please, enter the correctly format.')