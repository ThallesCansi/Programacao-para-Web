from os import system
import math
system('clear')

n1 = float(input('\033[1;34mDigite um número: \033[m'))

print(f'''\n\033[1;34mSeno: \033[m{math.sin(n1)}
\033[1;34mCosseno: \033[m{math.cos(n1)}
\033[1;34mTangente: \033[m{math.tan(n1)}''')
