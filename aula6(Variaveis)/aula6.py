"""
Iniciar com letra, pode conter  números, separar _, letras minúsculas
"""
nome = 'Fulano'
idade = 23
altura = 1.70
e_maior = idade > 18
peso = 52
imc = peso / (altura * altura)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É de maior:', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
