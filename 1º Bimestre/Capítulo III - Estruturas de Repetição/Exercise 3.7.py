sum = 0
number = 0
i = 0

while True:
    number = int(input('Type number: '))
    if (number < 0):
        break
    else:
        sum += number
        i += 1

print(f'Average of numbers: {sum / i}')