
try:
    # a = {}
    a = 1/0
    try:
        a = 2/0
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
# else:
#     print('Seu código foi executado com sucesso.')
#     print(a)
finally:
    a = ''

print(a)