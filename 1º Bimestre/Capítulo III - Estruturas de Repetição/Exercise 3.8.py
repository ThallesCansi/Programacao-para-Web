number = int(input('Type number: '))
factorial = 1

for i in range(number, 1, -1):
    factorial = factorial * i

print(f'Factorial of the number {number} is {factorial}')