"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#         6    5    4    3    2    1
print(lista[0:3])
print(lista[3:])
lista[5] = 'Qualquer outra coisa'
print(lista[-1]) # Último valor da lista
print(lista)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)

lista2.append('B')

lista2.insert(0, 'banana')
print(lista2)

lista2.pop()
print(lista2)

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(lista3[3:5])
print(max(lista3))
print(min(lista3))
print(lista3)

lista4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for valor in lista4:
    soma += valor
print(soma)

lista5 = ['String', True, 10, -20.5]
for elemento in lista5:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')


# Jogo de descobrir a palavra

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Letra certa. "{letra}" existe na palavra secreta.')
    else:
        print(f'Letra errada. "{letra}" não existe na palavra secreta.')
        digitadas.pop

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta # Concatenação de secreto_temporario e letra_secreta
        else:
            secreto_temporario += '*' # Concatenação de secreto_temporario e '*'

    if secreto_temporario == secreto:
        print(f'Você descobriu a palavra. A palavra era "{secreto_temporario}".')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Voçê ainda tem {chances} chances.')
    print()
