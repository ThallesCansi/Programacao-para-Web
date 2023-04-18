from os import system
system('clear')

distancia = float(input('\033[1;34mDigite a distância (m): \033[m'))
velocidade = float(input('\033[1;34mDigite a velocidade (m/s): \033[m'))

tempo = distancia / velocidade

print(f'\n\033[1;35mTempo para atingir solo: \033[m\033[31m{tempo:.2f} segundos\033[m')
