from os import system
system('clear')

n1 = 10
n2 = 5

print(f'''\033[1;34mSoma: \033[m{n1 + n2}
\033[1;34mSubtração: \033[m{n1 - n2}
\033[1;34mMultiplicação: \033[m{n1 * n2}
\033[1;34mDivisão: \033[m{n1 / n2}''')
