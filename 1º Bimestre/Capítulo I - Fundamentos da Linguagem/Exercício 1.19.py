from os import system
system('clear')

velocidade_final = float(input('\033[1;34mDigite a velocidade final do objeto (m/s): \033[m'))
velocidade_inicial = float(input('\033[1;34mDigite a velocidade inicial do objeto (m/s): \033[m'))
tempo = float(input('\033[1;34mDigite o tempo que o objeto levou (s): \033[m'))

aceleracao = (velocidade_final - velocidade_inicial) / tempo

print(f'\n\033[1;35mA aceleração do objeto foi de: \033[m\033[31m{aceleracao:.2f} m/s²\033[m')
