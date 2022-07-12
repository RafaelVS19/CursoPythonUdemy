# lists, tuples, str -> Sequences -> Iterável

nome = 'Luiz Otávio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('FOR')

for letra in gerador:
    print(letra)
    

try:
    print(next(iterador)) # L
    print(next(iterador)) # u
    print(next(iterador)) # i
    print(next(iterador)) # z
    print(next(iterador)) # O
    print(next(iterador)) # t
    print(next(iterador)) # á
    print(next(iterador)) # v
    print(next(iterador)) # i
    print(next(iterador)) # o
except:
    pass # exceção para quando o iterador não tiver mais letras na string para iterar



# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)

