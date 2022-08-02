# Mutável: Listas, dicionário
# Imutáveis: Tuplas, strings, números, True, False, None

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_de_clientes1 = ['Fabricio']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_de_clientes1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Paulo'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
