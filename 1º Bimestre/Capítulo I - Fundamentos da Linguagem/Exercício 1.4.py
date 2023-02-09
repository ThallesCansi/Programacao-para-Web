from os import system
system('clear')

peso = float(input('\033[1;34mDigite seu peso:\033[m '))
altura = float(input('\033[1;34mDigite sua altura:\033[m '))

print(f'\n\033[1;35mSeu índice de massa corporal (IMC) é: \033[m{peso / (altura * altura):.2f}')
