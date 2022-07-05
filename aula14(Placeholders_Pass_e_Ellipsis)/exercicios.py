"""
1.Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número: ")
try:
    numero = int(numero)
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é impar')
except:
    print('Não é um número inteiro')
# OUTRA SOLUÇÃO
numero_inteiro = input('Digite um número inteiro: ')
if numero_inteiro.isnumeric():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')
else:
    print('Isso não é um número inteiro.')

"""
2.Faça um programa que pergunte a hora ao usuário e, lembrando-se
ao horário descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite um horário (0-23): ')
try:
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Hora deve estar entre 0 e 23.')
    else:
        if hora <= 11:
            print('Bom dia.')
        elif hora <= 17:
            print('Boa tarde.')
        else:
            print('Boa noite.')
except:
    print('Este valor não é um número')
# OUTRA SOLUÇÃO
horario = input('Digite um horário (0-23): ')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horario deve estar entre 0 e 23.')
    else:
        if hora <= 11:
            print('Bom dia.')
        elif hora <= 17:
            print('Boa tarde.')
        else:
            print('Boa noite.')
else:
    print('Por favor, digite um horário entre 0 e 23.')

"""
3.Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 
letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é
muito grande". 
"""
nome = input('Digite seu nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')


