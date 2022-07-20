# https://docs.python.org/pt-br/3/library/exceptions.html

# def divide(n1,n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise
#
# try:
#     divisao = divide(2,0)
#     print(divisao)
# except ZeroDivisionError as error:
#     print(error)


def divide(n1,n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1/n2

try:
    print(divide(n1=2,n2=0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print('Log:',error)