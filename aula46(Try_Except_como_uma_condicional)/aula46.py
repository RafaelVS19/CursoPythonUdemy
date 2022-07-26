def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

numero = converte_numero(input('Digite um número: ')) # O input sempre retorna uma string então é necessário converter para int ou float
if numero is None:
    print('Erro: isso não é um número.')
else:
    print(numero * 3)