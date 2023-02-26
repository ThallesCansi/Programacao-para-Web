number = int(input('Type number: '))
primeNumber = True 

for i in range(2, number):
    if (number % i == 0):
        primeNumber = False
        break

if primeNumber:
    print(f'The number {number} is prime number!')
else:
    print(f"The number {number} isn't prime number :(")