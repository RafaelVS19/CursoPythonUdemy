"""
While/Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1
else:
    print('Cheguei no else.')
print('Isso será executado.')
#else só sera executado quando a condição do while for falsa,
# se tiver um break o else será pulado