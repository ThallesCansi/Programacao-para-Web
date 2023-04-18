def compose(f, g):
    return lambda x: f(g(x))

def square(x):
    return x ** 2

def plus(x):
    return x + 1

composeFunction = compose(square, plus)

number = int(input('Enter a number to calculate your composite function: '))

print(composeFunction(number))