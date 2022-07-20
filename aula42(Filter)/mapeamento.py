from dados import produtos, pessoas, lista

nova_lista = [x for x in lista if x > 5]
print(nova_lista)
nova_lista1 = filter(lambda x: x > 5, lista)
print(list(nova_lista))

print()

def filtra(produto):
    if produto['preço'] > 50:
        produto['é_caro'] = True
    return True

nova_lista2 = filter(filtra, produtos)

for produto in nova_lista2:
    print(produto)

print()

def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista3 = filter(filtra, pessoas)

for pessoa in nova_lista3:
    print(pessoa)