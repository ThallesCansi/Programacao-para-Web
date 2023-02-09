from os import system
import math
system('clear')

angulo = float(input('\033[1;34mDigite a medida de um ângulo em radianos: \033[m'))

graus = math.degrees(angulo)

print(f'\n\033[1;35mO valor do ângulo \033[1;33m{angulo}\033[m \033[1;35mem graus é: \033[m\033[31m{graus:.2f}\033[m')
