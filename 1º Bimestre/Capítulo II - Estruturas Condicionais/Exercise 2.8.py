string = input('Type anything: ')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
checkNumber = 0
checkFloat = 0

for number in string:
    if (number in numbers):
        checkNumber += 1
    elif (number in ['.']):
        checkFloat += 1
        if (checkFloat > 1):
            print("It's doesn't a real number")
            break
    else:
        print("It's doesn't a real number")
        break

if (checkNumber == (len(string) - 1)):
    print("It's a real number")