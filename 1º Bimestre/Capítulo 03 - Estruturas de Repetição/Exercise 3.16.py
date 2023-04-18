listNumbers = list()

for i in range(10):
    listNumbers.append(int(input('Type a number: ')))

higherNumber = listNumbers[0]
smallerNumber = listNumbers[0]

for i in range(len(listNumbers)):
    if (smallerNumber > listNumbers[i]):
        smallerNumber = listNumbers[i]
    if (higherNumber < listNumbers[i]):
        higherNumber = listNumbers[i]

print(f'Higher number typed: {higherNumber}\nSmaller number typed: {smallerNumber}')

# listNumbers.sort()

# print(listNumbers[0], listNumbers[-1])