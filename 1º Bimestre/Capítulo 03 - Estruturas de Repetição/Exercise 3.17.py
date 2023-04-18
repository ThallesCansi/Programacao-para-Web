listNumbers = list()
sortedList = list()

for i in range(10):
    listNumbers.append(int(input('Type a number: ')))

for i in range(len(listNumbers)):
    smallerNumber = listNumbers[0]
    for i in range(len(listNumbers)):
        if (smallerNumber > listNumbers[i]):
            smallerNumber = listNumbers[i]
    sortedList.append(smallerNumber)
    listNumbers.remove(smallerNumber)


print(f'Second largest number: {sortedList[-2]}\nSecond smallest number: {sortedList[1]}')

# listNumbers.sort()

# print(listNumbers[1], listNumbers[-2])