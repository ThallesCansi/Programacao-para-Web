from os import system
system('clear')

valor_inicial = float(input('\033[1;34mDigite o valor inicial investido: R$ \033[m'))
taxa_juros = float(input('\033[1;34mDigite a taxa de juros aplicada (%): \033[m'))
tempo = float(input('\033[1;34mDigite o tempo total (em meses) do investimento: \033[m'))

valor_final = (valor_inicial * taxa_juros * tempo) / 100 

print(f'\n\033[1;35mO valor final do investimento foi de: \033[m\033[31mR$ {valor_final + valor_inicial:.2f}\033[m')
