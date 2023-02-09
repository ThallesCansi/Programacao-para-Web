from os import system
system('clear')

membros_familia = list()
# membros_familia = ['Joemar', 'Alessandra', 'Jean', 'Lara', 'Thalles']

print('\033[1;34mMembros da família\033[m')
for i in range(1, 6):
    nome = input(f'\033[1;34mPessoa {i}: \033[m')
    membros_familia.append(nome)

print(f'\n\033[1;34mOs membros da família são: \033[m\033[31m{membros_familia}\033[m')
