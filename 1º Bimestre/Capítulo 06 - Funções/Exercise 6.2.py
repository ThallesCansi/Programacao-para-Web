def evenOdd(number):
    return True if (number % 2 == 0) else False

number = int(input('Enter a number: '))

print(f'The number entered is even: {evenOdd(number)}')