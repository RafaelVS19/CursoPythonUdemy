"""
Desempacotamento de Listas
"""
lista = ['Luiz', 'João', 'Maria',1,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista # *outra_lista gera outra lista para o resto dos valores

print(n1, n2, n3, outra_lista, ultimo_da_lista)