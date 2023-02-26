f0 = 0
f1 = 1

number = int(input('Type a number: '))

if (number < 0):
    print('Incorrect input entered')
elif (number == 0):
    print(f'{f0}')
elif (number == 1):
    print(f'{f1}')
else:
    for i in range(2, number):
        fn = f0 + f1
        f0 = f1
        f1 = fn

print(f'The nth term of the sequence is: {f1}')