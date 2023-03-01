string = input('Write a sentence: ')

splitString = string.split()

newString = []
for i in splitString:
    newString.append(i.strip())

print(' '.join(newString))