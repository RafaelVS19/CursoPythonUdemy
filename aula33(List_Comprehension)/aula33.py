l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
print(ex1)

print()

ex2 = [v * 2 for v in l1]
print(ex2)

print()

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

print()

l2 = ['Luiz','Mauro','Maria']
ex4 = [v.replace('a','@').upper() for v in l2]
print(ex4)

print()

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(x, y) for x, y in tupla]
ex5 = dict(ex5)
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]