"""
Operadores Lógicos
and, or, not
in e not in
"""
# verdadeiro E verdadeiro = verdadeiro
# verdadeiro E falso = falso
# comparacao1 and comparacao2

# verdadeiro OU verdadeiro = verdadeiro
# verdadeiro OU falso = verdadeiro
# comparacao1 or comparacao2

a = ''
b = 1
if not b:
    print('Por favor, preencha o valor de A.')

nome = 'João Silva'
if 'Joã' in nome:
    print('Existe.')
else:
    print('Não existe')

nome = 'João Silva'
if 'Sil' not in nome:
    print('Executei.')
else:
    print('Existe o texto.')

############

usuario = input('Nome do usuário: ')
senha = (input('Senha do usuário: '))

usuario_bd = 'joão'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')


