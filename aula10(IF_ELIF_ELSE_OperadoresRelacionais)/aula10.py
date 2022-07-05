"""
Operadores relacionais
 == > < => <= !=
"""
num1 = 2 #int
num2 = 2 #int

expressao = (num1 == num2)
print(expressao)

expressao = (num1 > num2)
print(expressao)

expressao = (num1 >= num2)
print(expressao)

expressao = (num1 <= num2)
print(expressao)

var1 = 'João'
var2 = 'Pedro'
expressao = (var1 != var2)
print(expressao)

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Limite para pegar emprestimo
idade_menor = 20 #muito jovem
idade_maior = 30 #passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')