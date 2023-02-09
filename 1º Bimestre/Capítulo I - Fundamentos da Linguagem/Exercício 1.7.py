from os import system
system('clear')

nome_produto = input('\033[1;34mDigite o nome do produto: \033[m')
preco_custo = float(input('\033[1;34mDigite o preço de custo: \033[m'))
preco_venda = float(input('\033[1;34mDigite o preço de venda: \033[m'))
quantidade_estoque = float(input('\033[1;34mDigite a quantidade em estoque do produto: \033[m'))

lucro = (preco_venda - preco_custo) * quantidade_estoque

print(f'\n\033[1;35mO lucro que o estoque pode gerar com o produto\033[m \033[1;33m{nome_produto}\033[m \033[1;35mé de: \033[mR$ {lucro:.2f}')
