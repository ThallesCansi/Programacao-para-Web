from os import system
system('clear')

largura = float(input('\033[1;34mDigite a largura do retângulo: \033[m'))
altura = float(input('\033[1;34mDigite a altura do retângulo: \033[m'))

print(f'\n\033[1;35mÁrea: \033[m\033[31m{largura * altura:.2f}\033[m \n\033[1;35mPerímetro: \033[m\033[31m{(largura * 2) + (altura * 2):.2f}')
