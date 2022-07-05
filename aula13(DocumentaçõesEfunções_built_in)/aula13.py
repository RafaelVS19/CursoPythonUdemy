
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# isnumeric isdigit isdecimal
# checar se são números e positivos
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não foi possivel converter os números para realizar a conta')

####################
# para contonar o erro ao digitar uma string e não poder ser convertida
num3 = input('Digite um número: ')
num4 = input('Digite outro número: ')

try:
    num3 = float(num3)
    num4 = float(num4)
except:
    print('ERROR')

