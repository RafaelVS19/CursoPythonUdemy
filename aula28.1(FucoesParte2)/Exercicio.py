"""
1. Crie uma função que exibe uma saudação com os parametros saudação
e nome.
"""
def mensagem(saudacao,nome):
    print(f'{saudacao} {nome}')

mensagem('Bom dia', 'João')

"""
2. Crie uma função que recebe 3 números como parametros e exiba a soma
entre eles.
"""
def soma(n1,n2,n3):
    print(n1 + n2 + n3)

soma(3,4,25)

"""
3. Crie uma função que receba 2 números. O primeiro é um valor e o é 
percentual (ex 10%). Retorne (return) o valor do primeiro numero somado
do aumento do percentual do mesmo.
"""
def p (valor,percentual):
    aumento = valor * percentual / 100
    return valor + aumento

resultado = p(15,100)
print(resultado)

"""
4. Fizz Buzz - Se o parametro da função for divisível por 3, retorne fizz,
se o parametro da função for divisivel por 5, retorne buzz. Se o parametro
da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, 
retorne o número enviado. 
"""
def divisao(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return num

resultado = divisao(7)
print(resultado)