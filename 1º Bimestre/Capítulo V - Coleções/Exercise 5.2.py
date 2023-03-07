string = input('Write anything: ')

wordsWithO = [word.replace('a', 'o') for word in string.split() if 'a' in word]

print(wordsWithO)