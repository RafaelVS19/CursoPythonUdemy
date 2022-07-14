"""
Zip - Unindo iteráveis
Zip_longest - precisa ser importado do módulo Itertools
"""
from itertools import zip_longest, count

indice = count() # contador de números
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidade_estados = zip(indice, estados, cidades)

for indice, estados, cidades in cidade_estados:
    print(indice, estados, cidades)

print()

cidade_estados2 = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidade_estados2))