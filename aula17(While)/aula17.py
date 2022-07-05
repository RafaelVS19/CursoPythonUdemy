"""
while em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.
"""
"""
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue

    print(x)
    x += 1
print('Acabou')


y = 0
while y < 10:
    if y == 3:
        y += 1
        break

    print(y)
    y += 1
print('Acabou')

#tabelas
x1 = 0 #coluna
while x1 < 10:
    y1 = 0  # linha
    while y1 < 5:
        print(f'({x1} , {y1})')
        y1 += 1

    x1 += 1

print('Acabou')
"""

while True:
    print()
    num1 = input('Digite um numero ou SAIR para encerrar! ')
    if num1 == 'SAIR':
        break
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar números.')

    num1 = int(num1)
    num2 = int(num2)

    # + - * /
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Operador invalido')

