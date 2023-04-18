number = list()

def higherNumber(number):
    higherNumberList = number[0]

    for i in number:
        if (i > higherNumberList):
            higherNumberList = i
    return higherNumberList

    
while True:
    number.append(int(input('Enter a number: ')))
    if (number[-1] == 0):
        break

print(f'{higherNumber(number)}')