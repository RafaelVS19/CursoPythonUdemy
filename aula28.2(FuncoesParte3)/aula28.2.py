"""
Funções - *args **kwargs
"""
def funcao(*args, **kwargs):
    # args = list(args) - transformar em lista para poder alterar valores
    print(args)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
funcao(*lista, *lista2, nome='Luiz', sobrenome='Silva', idade='30')

