n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))

if (n1 % n2 == 0):
    print(f'The number {n1} is divisible by {n2}')
else:
    print(f"The number {n1} isn't divisible by {n2}")