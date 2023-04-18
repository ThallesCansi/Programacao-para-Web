from os import system
import math
system('clear')

r = float(input('\033[1;34mDigite o raio do círculo: \033[m'))

perimetro = 2 * math.pi * r

print(f'\n\033[m\033[1;35mPerímetro:\033[m \033[31m{perimetro:.2f}\033[m')
