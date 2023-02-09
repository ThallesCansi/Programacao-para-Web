import os
os.system('clear')

conjunto1 = {'gato', 'cachorro', 'elefante', 'girafa'}
conjunto2 = {'macaco', 'zebra', 'cobra',  'elefante'}

print(f'\033[1;34mUnião: \033[m\033[31m{conjunto1 | conjunto2}\033[m')
print(f'\033[1;34mInterseção: \033[m\033[31m{conjunto1 & conjunto2}\033[m')
print(f'\033[1;34mDiferença: \033[m\033[31m{conjunto1 - conjunto2}\033[m')