keys = input('Enter a space-separated list of keys: ').split()

values = input('Enter a space-separated list of values: ').split()

evens = zip(keys, values)

dic = dict(evens)

print(dic)