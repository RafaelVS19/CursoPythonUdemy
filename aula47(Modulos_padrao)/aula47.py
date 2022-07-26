# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html
from sys import platform as pl
print(pl)

print()

import random
for i in range(10):
    print(random.randint(0,10))

print()

