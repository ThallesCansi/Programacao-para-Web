file = open('file.txt', 'r')

reversedFile = open('reversedFile.txt', 'w')

for i in file:
    row = i.strip()[::-1] + '\n'
    reversedFile.write(row)

file.close()
reversedFile.close()