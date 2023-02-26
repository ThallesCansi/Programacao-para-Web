string = input('Type anything: ')

month = list()
day = list()
year = int()

for i in range(1, 32):
    if (i <= 12):
        month.append(i)
    day.append(i)

# Firstly, check if type in correctly format


# Check if type year is leap year
# year = string[]
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(f'The year {year} is leap year')
else:
    print(f'The year {year} is not leap year')