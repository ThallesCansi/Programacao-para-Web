from os import system
system('clear')

distancia = float(input('\033[1;34mDigite a distância percorrida pelo objeto (m): \033[m'))
tempo = float(input('\033[1;34mDigite o tempo gasto pelo objeto (s): \033[m'))

velocidade = distancia / tempo

print(f'\n\033[1;35mO valor da velocidade média do objeto é de: \033[m\033[31m{velocidade:.2f} m/s\033[m')
