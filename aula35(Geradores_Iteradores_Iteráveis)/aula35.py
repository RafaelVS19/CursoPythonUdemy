lista = [0,1,2,3,4,5]
# print(hasattr(lista, '__iter__')) # saber se alista é iterável

lista = iter(lista) # transformou a lista em iterador

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print()

import sys
import time
#
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
#
# for v in g:
#     print(v)

print()

l1 = [x for x in range(100)] # forma simples de fazer um gerador
print(type(l1))
print(sys.getsizeof(l1)) # .getsizeof para saber quantos bytes usa da memória
l2 = (x for x in range(100))
print(type(l2))
print(sys.getsizeof(l2))

for v in l2:
    print(v)