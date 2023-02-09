from os import system
import math
system('clear')

r = float(input('\033[1;34mDigite o raio do círculo: \033[m'))

area_circulo = math.pi * r ** 2
comprimento = 2 * math.pi * r

print(f'\n\033[1;35mA área do círculo equivale à\033[m \033[31m{area_circulo:.2f}\033[m\033[1;35m e o seu perímetro é:\033[m \033[31m{comprimento:.2f}\033[m')
