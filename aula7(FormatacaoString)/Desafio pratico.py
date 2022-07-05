nome = 'Fulano'
idade = 23
altura = 1.70
peso = 54.0
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
