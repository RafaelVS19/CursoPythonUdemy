from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

print()

soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(soma_precos / len(produtos))

print()

soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades / len(pessoas))

