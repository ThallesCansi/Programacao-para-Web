words = input('Enter a comma-separated list of names: ').split(', ')

lengths = list(map(len, words))

print(lengths)