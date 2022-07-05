"""
Continuação:
Funções - def
"""
def divisao(n1,n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Conta inválida')

print(' ')

def dumb():
    return 'João', 'Silva'

var = dumb()
print(var[0], type(var))