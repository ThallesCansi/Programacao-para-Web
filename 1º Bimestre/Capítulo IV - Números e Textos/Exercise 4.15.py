string = input('Type anything: ')
words = string.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word, amount in count.items():
    print(f"A word '{word}' aparece {amount} vezes na string.")