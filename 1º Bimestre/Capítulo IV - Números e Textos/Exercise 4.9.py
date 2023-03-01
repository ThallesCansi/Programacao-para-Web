string = input('Write a sentence')
existWord = input('Type word exist in string: ')
newWord = input('Type new word for replace: ')

newString = string.replace(existWord, newWord)

print(f'New string is: {newString}')