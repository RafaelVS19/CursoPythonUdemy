nome = 'Fulano'
idade = 23
altura = 1.70
e_maior = idade > 18
peso = 52
imc = peso / (altura * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos  e seu imc é {:.2f}'. format(nome, idade, imc))
print('{n} tem {i} anos  e seu imc é {im:.2f}'. format(n=nome, i=idade, im=imc))

