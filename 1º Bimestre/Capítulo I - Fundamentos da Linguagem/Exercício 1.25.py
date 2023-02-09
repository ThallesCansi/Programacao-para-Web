from os import system
from math import pi
system('clear')

r = float(input('\033[1;34mDigite o raio da esfera: \033[m'))

volume = (4 * pi * r ** 3) / 3

print(f'\n\033[m\033[1;35mVolume:\033[m \033[31m{volume:.2f}\033[m')
