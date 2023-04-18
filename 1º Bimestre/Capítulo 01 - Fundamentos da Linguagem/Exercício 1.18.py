from os import system
system('clear')

massa = float(input('\033[1;34mDigite a massa do objeto (kg): \033[m'))
aceleracao = float(input('\033[1;34mDigite a aceleração do objeto (m/s): \033[m'))

print(f'\n\033[1;35mA força resultante é de: \033[m\033[31m{massa * aceleracao:.2f} N\033[m')
