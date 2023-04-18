names = input('Enter a comma-separated list of names: ').split(', ')

upperNames = list(map(str.upper, names))

print(upperNames)