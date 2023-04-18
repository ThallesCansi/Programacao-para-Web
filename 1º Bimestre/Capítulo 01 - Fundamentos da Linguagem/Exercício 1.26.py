from os import system
system('clear')

cateto1 = float(input('\033[1;34mDigite o valor do primeiro cateto: \033[m'))
cateto2 = float(input('\033[1;34mDigite o valor do segundo cateto: \033[m'))

area = (cateto1 * cateto2) / 2

print(f'\n\033[m\033[1;35mA área do triângulo retângulo equivale à:\033[m \033[31m{area:.2f}\033[m')
