from os import system
system('clear')

distancia = float(input('\033[1;34mDigite a distância percorrida pelo objeto (m): \033[m'))
tempo = float(input('\033[1;34mDigite o tempo gasto pelo objeto (s): \033[m'))
aceleracao = float(input('\033[1;34mDigite a aceleração do objeto (m/s²): \033[m'))

velocidade_inicial =  (((aceleracao * tempo ** 2) / 2) - distancia) / tempo
velocidade_final = velocidade_inicial + (aceleracao * tempo)

print(f'\n\033[1;35mVelocidade inicial: \033[m\033[31m{velocidade_inicial:.2f} m/s \n\033[m\033[1;35mvelocidade final: \033[m\033[31m{velocidade_final:.2f} m/s\033[m')
