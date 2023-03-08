fileName = input('Enter name of file: ')

file = open(fileName, 'r')
print(file.read())
file.close()