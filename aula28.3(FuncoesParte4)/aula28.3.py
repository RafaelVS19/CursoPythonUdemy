variavel = 'valor'

def func():
    print(variavel)

def func2(arg=None):
    arg = arg.replace('v','c')
    return arg

func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)
#########################################
def func3():
    outra_variavel = 'João Silva'
    return outra_variavel

def func4(arg):
    print(arg)

var = func3()
func4(var)