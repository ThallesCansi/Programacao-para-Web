import shutil

file = input('Enter name of file: ').split('.')

shutil.copy(file[0] + '.' + file[1], file[0] + '.copy' + '.' + file[1])