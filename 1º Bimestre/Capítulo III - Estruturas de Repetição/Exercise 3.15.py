number = int(input('Type number: '))
sum = 0

for i in range(number -1, 0, -1):
    if (number % i == 0):
        sum += i

if (sum == number):
    print("It's perfect number!")
else:
    print("Isn't perfect number!")