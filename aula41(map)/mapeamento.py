from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)

nova_lista1 = [x * 2 for x in lista]

print(list(nova_lista))
print(nova_lista1)

print()

def aumenta_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p

precos = map(lambda p: p['preço'], produtos)
for preco in precos:
    print(preco)

print()

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

print()

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)