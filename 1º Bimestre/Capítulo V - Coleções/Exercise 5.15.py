numbers = input('Enter a semicolon-separated list of numbers: ').split('; ')

numbers = [int(number) for number in numbers]

reference = int(input('Enter a reference number: '))

for i in range(len(numbers)):
    if numbers[i] > reference:
        print(f'The first element greater than {reference} is at position {i}.')
        break
else:
        print(f'No list element is greater than {reference}.')