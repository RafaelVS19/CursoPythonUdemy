#Não pode alterar os valores de uma tupla
t1 = (1,2,3, 'a', 'João')
t2 = 6,7,8,9,10 #tupla sem parenteses
t3 = t1 + t2

print(type(t1))
print(t1)

for v in t1:
    print(v)

print(t1[2:])

print(t3)

# t1[1] = 3 # erro pois não se pode alterar valores de uma tupla

t4 = (1,2,3,4,5)
t4 = list(t4) # conversão de uma tupla para lista
t4[1] = 3000
t4 = tuple(t4) # conversão da lista de volta para uma tupla

print(t4)

