import os

file = input('Enter name of file: ')

os.rename(file + '', 'renamed' + file + '.txt')