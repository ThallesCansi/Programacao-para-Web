def fiterList(listOne, functionOne):
    return list(filter(functionOne, listOne))

listOne = [1, 2, 3, 4, 5, 6]
functionOne = lambda x: x % 2 == 0

newListOne = fiterList(listOne, functionOne)

print(newListOne)