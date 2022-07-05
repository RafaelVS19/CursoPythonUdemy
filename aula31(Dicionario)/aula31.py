# Cada chave precisa ser única
d1 = {'chave1':'valor da chave'}
d1 ['nova_chave'] = 'valor da nova chave'

print(d1)
print(d1['chave1'])

print(' ')

d2 = {1:'valor1', 2:'valor2', 3:'valor3'}
print(d2)
print(d2[3])

print(' ')

d1.update(d2)
print(f'Contatenando d1 e d2: {d1}')

print(' ')

# Outro método de criar dicionários
d2 = dict(chave1='valor da chave', chave2='Valor da outra chave')
print(d2)

print(' ')

d3 = {
    'str':'valor',
    123:'outro_valor',
    (1,2,3,4):'Tupla no dicionário',
}
print(d3[(1,2,3,4)])

if 'chavenaoexiste' not in d3:
    print('chave_não_existe')

if d3.get('nomedachave') is not None:
    print(d3.get('nomedachave'))

# d3.update({'nova_chave':'novo_valor'})
# print(d3)

print(' ')

# del d3['str']
print(d3)
print('str' in d3)
print('str' in d3.keys())
print('outro_valor' in d3.values())

print(len(d3))

print(' ')

d4 = {
    'chave1':'valor',
    'chave2':'outro valor',
    'chave3':'João'
}
for valor in d4.values():
    print(valor)
for k, v in d4.items(): # mostra as chaves e valores
    print(k, v)

print(' ')

clientes = {
    'cliente1': {
      'nome':'João',
      'sobrenome':'Silva',
    },
    'cliente2': {
        'nome': 'Paulo',
        'sobrenome':'Silva',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome':'Silva',
    }

}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v}') # \t para deixar identado

print(' ')

import copy # importa o modulo do python
dicionario = {1:'a', 2:'b', 3:'c', 'd':['Fulano', 'Silva']}
v = copy.deepcopy(dicionario) # gera uma cópia para não alterar o primeiro dicionário

v[1] = 'Luiz'
v['d'][0] = 'Joãozinho'

print(dicionario)
print(v)
dicionario.popitem() # elimina o último item
print(dicionario)

print(' ')

# transformar uma lista em dicionário
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
dicio = dict(lista) # dict converte para dicionario
print(dicio)

