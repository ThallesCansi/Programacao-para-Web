numbers = list()
even = 0
odd = 0

for i in range(5):
    numbers.append(int(input('Type a number: ')))

for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        even += 1
    else:
        odd += 1

if (even == len(numbers)):
    print('All numbers entered are even!')
else:
    print(f'{odd} odd number was entered!')