"""
Manipulando strings
* String indices
* Fatiamento de strings (inicio:fim:passo)
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser acessadas diretamente em cada tipo.

https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
# positivos indices [P=0, y=1, t=2, h=3, o=4, n=5, _=6, 3=7]
texto = 'Python_3'
print(texto[4])
# negativos indices [87654321]

#fatiamento

#nova_string = texto[2:6]
#nova_string = texto[7:]
#nova_string = texto[-1]
nova_string = texto[0::3]
print(nova_string)

print(len(texto))