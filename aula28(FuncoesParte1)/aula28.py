"""
Funções - def
"""
def saudacao01(msg='Olá', nome='usuário'):
    return f'{msg} {nome}'

variavel = saudacao01()
print(variavel)

print(' ')

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Bom dia,', 'João')
saudacao('Boa tarde,', 'Maria')

print(' ')

def saudacao2(msg='Olá', nome='João'):
    print(msg, nome)

saudacao2()

