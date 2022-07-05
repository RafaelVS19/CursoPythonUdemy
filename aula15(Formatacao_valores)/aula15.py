"""
Formatando valores com modificadores

:s - texto(strings)
:d - inteiros ou digit(int)
:f - números de ponto flutuante(float)
:.(NÚMERO)f - quantidade de casas decimais(float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'João Silva'
print(f'{nome:s}')
print(len(nome))
# Formatação f'{}'
print(f'{nome:#^50}')
#Outro jeito de formartar '{}'.format()
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #primeiras letras maiusculas

num3 = 1
print(f'{num3:0>10}')
num4 = 1150
print(f'{num4:0^10}')
print(f'{num4:0<10}')
print(f'{num4:0>10.2f}')

#acessar pelo indice
nome1 = 'João'
sobrenome = 'Silva'
nome_formatado1 = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado1)
