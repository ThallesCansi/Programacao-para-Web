numbers = input('Enter a comma-separated list of numbers: ').split(', ')
numbers = [float(num) for num in numbers]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)