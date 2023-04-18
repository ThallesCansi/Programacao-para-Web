from os import system
system('clear')

n1 = float(input('\033[1;34mNúmero 1:\033[m '))
n2 = float(input('\033[1;34mNúmero 2:\033[m '))

print(f'\n\033[1;35mA potência de\033[m \033[1;33m{n1}\033[m \033[1;35melevado à\033[m \033[1;33m{n2}\033[m \033[1;35mé: \033[m{n1 ** n2}')
