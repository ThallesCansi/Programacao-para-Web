from os import system
system('clear')

a = float(input('\033[1;34mDigite a medida do primeiro lado do triângulo: \033[m'))
b = float(input('\033[1;34mDigite a medida do segundo lado do triângulo: \033[m'))

hip = ((a ** 2) + (b ** 2)) ** (1 / 2)

print(f'\n\033[1;35mO valor da hipotenusa desse triângulo é: \033[m\033[31m{hip:.2f}\033[m')
