string = input('Write a sentence: ')

for i in range(0, len(string), 6):
    print(string[i:i+6])