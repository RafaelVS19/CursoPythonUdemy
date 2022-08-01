# https://docs.python.org/3/library/functions.html#open

import os
import json

# Para remover os arquivos
# os.remove('abc.txt')
# os.remove('abcd.txt')
# os.remove('abc.json')

file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())

print('###############')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('###############')

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()

print('###############')

with open('abcd.txt', 'w+') as file1:
    file1.write('Linha 1\n')
    file1.write('Linha 2\n')
    file1.write('Linha 3\n')
    file1.seek(0)
    print(file1.read())

with open('abcd.txt', 'r') as file1:
    print(file1.read())

with open('abcd.txt', 'a+') as file1: # ' a ' é o append no arquivo, a edição no final do arquivo
    file1.write('Linha 4\n')
    file1.seek(0)
    print(file1.read())

print('###############')

d1 = {
    'Pessoa1':{
        'nome':'Luiz',
        'idade': 25,
    },
    'Pessoa2':{
        'nome':'Maria',
        'idade': 30,
    }
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file2:
    file2.write(d1_json)

print(d1_json)