# Sets somente suportam valores e usa-se '{}' para criar
# não aceita elementos repetidos
# add (adiciona), update(atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentos nos dois sets)
# difference - (elementos apenas no set da esquerda)
# simmetric_diference ^ (elementos que estão nos dois sets, mas não em ambos)

s = set()
s.add(1)
s.add(2)
s.discard(2)
s.update([1,2,3,4,5,6], {5,6,7,8})
print(s)

print()

# remover elementos repetidos de uma lista,convertendo para set e
# depois retornando para lista
l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9,'Fulano','Fulano']
l1 = set(l1)
l1 = list(l1)
print(l1)

print()

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2 # união dos sets
s4 = s1 & s2 # interseção dos sets
s5 = s1 - s2 # elementos que aparece apenas no set da esquerda
s6 = s1 ^ s2 # elementos que estão nos dois sets, mas não em ambos
print(s3)
print(s4)
print(s5)
print(s6)

print()


lista1 = ['João', 'Maria', 'Ana']
lista2 = ['João', 'Maria', 'Maria', 'Ana'
          , 'Ana', 'Ana', 'Ana', 'Ana', 'Ana', 'Ana', 'Ana']

if set(lista1) == set(lista2):
    print('Lista1 é igual a Lista2')
else:
    print('Lista1 é diferente de Lista2')