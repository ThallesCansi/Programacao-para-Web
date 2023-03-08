import os

os.mkdir('temp')

path = r'./temp/tempfile.txt'

with open(path, 'w') as file:
    file.write('')