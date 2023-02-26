wordList = list()
invertedList = list()

string = input('Type anything: ').replace(' ', '')

for i in string:
    wordList.append(i)

for i in wordList:
    invertedList.insert(0, i)

if (wordList == invertedList):
    print('This is a palindrome')
else:
    print("This ins'n a palindrome")