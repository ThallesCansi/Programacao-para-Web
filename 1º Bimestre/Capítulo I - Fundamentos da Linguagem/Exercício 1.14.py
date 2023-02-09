from os import system
system('clear')

base = float(input('\033[1;34mDigite a base do triângulo: \033[m'))
altura = float(input('\033[1;34mDigite a altura do triângulo: \033[m'))

print(f'\n\033[1;35mÁrea do triângulo: \033[m\033[31m{(base * altura) / 2:.2f}\033[m')
