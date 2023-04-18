from os import system
system('clear')

nome = input('\033[1;34mDigite seu nome: \033[m')
salario = float(input('\033[1;34mDigite o valor do seu salário: \033[mR$ '))
imposto = float(input('\033[1;34mDigite o valor do seu imposto (%): \033[m'))

salario_liquido = salario - (salario * (imposto / 100))

print(f'\n\033[m\033[1;35mFuncionário:\033[m \033[31m{nome}\033[m \n\033[m\033[1;35mSalário Líquido:\033[m \033[31m{salario_liquido}\033[m')
