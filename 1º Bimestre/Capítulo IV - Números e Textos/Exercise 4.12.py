string = input('Write a sentence: ')

countA = 0
countO = 0

splitString = string.split(' ')

for i in splitString:
    if (i.endswith('o') == True):
        countO += 1
    if (i.startswith('a') == True):
        countA += 1

print(f'The number of words that end with the letter o is {countO}')
print(f'The number of words start with the letter a is {countA}')