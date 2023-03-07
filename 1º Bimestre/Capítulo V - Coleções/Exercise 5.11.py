numbers = input('Enter a semicolon-separated list of numbers: ').split('; ')

evenNumbers = [int(numero) for numero in numbers if int(numero) % 2 == 0]

print(evenNumbers)