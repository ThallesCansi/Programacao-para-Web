factorial = 1

number = int(input('Type a number: '))

if (number < 0):
    print('Please, type natural number')
elif (number == 0):
    print('Factorial of 0 is 1')
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f'Factorial of number {number} is: {factorial}')