from os import system
system('clear')

preco_mercadoria = float(input('\033[1;34mDigite o preço da mercadoria: \033[mR$ '))
desconto = float(input('\033[1;34mDigite o desconto da mercadoria (%): \033[m'))
imposto = float(input('\033[1;34mDigite o imposto da mercadoria (%): \033[m'))

preco_imposto = (preco_mercadoria * imposto / 100) + preco_mercadoria

preco_final = preco_imposto - (preco_imposto * desconto / 100)

print(f'\n\033[1;35mO valor final do produto foi de: \033[m\033[31mR$ {preco_final:.2f}\033[m')
