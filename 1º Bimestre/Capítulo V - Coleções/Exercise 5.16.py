numbers = input('Enter a semicolon-separated list of numbers: ').split('; ')
numbers = [int(x) for x in numbers]

for i in range(len(numbers)):
    if i % 2 == 0:
        numbers[i:i+2] = numbers[i:i+2][::-1]

print(numbers)