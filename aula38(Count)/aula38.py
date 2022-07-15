# # Para corrigir uma aula anterior - Zip não é um gerador
# from types import GeneratorType
# variavel = ((x, y) for x ,y in zip('Alo', 'Alo'))
# print(isinstance(variavel, GeneratorType)) # checa se a instancia é de um gerador

"""
count - itertools
"""

from itertools import count

contador = count(start=5, step = 2)
# contador = count(start=9, step= -1)

for valor in contador:
    print(round(valor, 2)) # round para arredondar para 2 casas decimais

    if valor >= 10 or valor <= -10:
        break

print()

contador1 = count()
lista = ['João', 'Maria', 'Ana', 'José', 'Silva']
lista = zip(contador1, lista)
print(list(lista))