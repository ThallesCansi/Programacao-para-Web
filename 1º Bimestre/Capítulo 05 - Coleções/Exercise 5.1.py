numbers = []

for i in range(20):
    numbers.append(i)

squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)