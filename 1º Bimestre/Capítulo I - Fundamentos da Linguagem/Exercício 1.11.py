from os import system
system('clear')

a = float(input('\033[1;34mDigite o primeiro coeficiente (a): \033[m'))
b = float(input('\033[1;34mDigite o primeiro coeficiente (b): \033[m'))
c = float(input('\033[1;34mDigite o primeiro coeficiente (c): \033[m'))

delta = (b ** 2) - (4 * a * c)

if (delta < 0):
    print('\033[1;35mNão existe raiz real\033[m')
else:
    x1 = (- b + (delta ** (1 / 2))) / (2 * a)
    x2 = (- b - (delta ** (1 / 2))) / (2 * a)
    print(f'\n\033[1;35mAs raízes da equação é:\033[m \n\033[31mx₁ = {x1:.2f} \nx₂ = {x2:.2f}\033[m')
