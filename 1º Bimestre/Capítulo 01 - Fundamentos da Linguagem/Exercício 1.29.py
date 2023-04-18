from os import system
system('clear')

lista_membros = list()
familia = dict()
# familia = [{'nome': 'Joemar',     'idade': 60, 'cor dos olhos': 'Castanhos'},
#            {'nome': 'Alessandra', 'idade': 50, 'cor dos olhos': 'Pretos'},
#            {'nome': 'Jean',       'idade': 26, 'cor dos olhos': 'Pretos'},
#            {'nome': 'Lara',       'idade': 22, 'cor dos olhos': 'Castanhos'},
#            {'nome': 'Thalles',    'idade': 19, 'cor dos olhos': 'Castanhos'}]

for i in range(1, 6):
    print('\033[1;34mMembros e características da família\033[m')
    familia.clear()
    familia['nome'] = input(f'\033[1;34mPessoa {i}: \033[m')
    familia['idade'] = int(input(f'\033[1;34mIdade do(a) {familia["nome"]}: \033[m'))
    familia['cor dos olhos'] = input(f'\033[1;34mCor dos olhos do(a) {familia["nome"]}: \033[m')
    lista_membros.append(familia)
    familia = familia.copy()
    system('clear')

print(f'\n\033[1;34mOs membros da família são: \033[m\033[31m{lista_membros}\033[m')
