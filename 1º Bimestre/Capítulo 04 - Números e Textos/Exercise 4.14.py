string = input('Type anything: ')
words = string.split() 
positions = []

for i in words:
    posicao = string.find(i)
    positions.append(posicao)

for i, word in enumerate(words):
    print(f"The word '{word}' start in position {positions[i]} of string.")