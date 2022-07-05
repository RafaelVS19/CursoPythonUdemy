"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

# texto = 'Python'
# for letra in texto:
#     print(letra)

# for numero in range(0, 11, 1):
#     print(numero)
# for numero in range(0, 11, 3): # Multiplos de 3
#      print(numero)
# for numero in range(20, 10, -1):
#     print(numero)

texto = 'Python'
nova_string = ''
for letra in texto:
     if letra == 't':
         nova_string += letra.upper()
     elif letra == 'h':
         nova_string += letra.upper()
     else:
         nova_string +=letra

print(nova_string)


