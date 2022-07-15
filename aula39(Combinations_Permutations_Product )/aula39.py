"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ('Fulano', 'João', 'Ana', 'Fabricio', 'Paulo', 'José')

# por exemplo: ele considera ('Fulano','André') e ('André','Fulano')
# a mesma coisa pois a ordem não importa

for grupo in combinations(pessoas, 2):
    print(f'combinations:{grupo}')

print()

# por exemplo: ele considera ('Fulano','André') e ('André','Fulano')
# diferentes pois a ordem importa
for grupo1 in permutations(pessoas, 2):
    print(f'permutations:{grupo1}')

print()

# por exemplo: ele considera ('Fulano','André') e ('André','Fulano')
# diferentes pois a ordem importa e pode repetir valores como ('Fulano','Fulano')
for grupo2 in product(pessoas, repeat=2):
    print(f'product:{grupo2}')