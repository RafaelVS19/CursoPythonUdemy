"""
For/Else
"""
# variavel = ['João', 'Maria', 'Luiz']
# for valor in variavel:
#    # if valor.startswith('J'):
#    #     print('Começa com J', valor)
#    # else:
#    #     print('Não começa com J', valor)

variavel = ['Luiz', 'Joãozinho', 'Maria']

comeca_com_J = False
for valor in variavel:
    if valor.lower().startswith('j'): # .lower torna as letras para minusculas e .startswith verifica se começa com j
        continue # esse continue pula a condicional 'if' se valor igual a letra j e vai para o print
    print(valor)
