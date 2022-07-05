"""
Split, Join e Enumerate
* Split - divide uma string # str
* Join - junta uma lista # str
* Enumerate - enumera elementos da lista # str
"""
# Função SPLIT
string = 'O Brasil é o o o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem} vezes)')
print(' ') # Só para dar um espaço
for valor in lista_2:
    print(valor.strip().capitalize())

print(' ')

# Função JOIN
string1 = 'O Brasil é penta.'
lista = string1.split(' ')
string2 = ','.join(lista)

print(string2)
print(' ')

# Função ENUMERATE
string2 = 'O Brasil é penta.'
lista01 = string1.split(' ')

for indice, valor in enumerate(lista01):
    print(indice, valor)
print(' ')

#Enumerate Lista dentro de outra lista
lista02 = [
      # 0     # 1    # 2
    ['Edu', 'João', 'Luiz'], # lista com indice 0
    ['Maria', 'Aline', 'Joana'], # lista com indice 1
    ['Helena', 'Paulo', 'Henrique'], # lista com indice2
]
enumerada = list(enumerate(lista02))
print(enumerada[1][1][2])
print(' ')

for v1 in enumerate(lista02, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)