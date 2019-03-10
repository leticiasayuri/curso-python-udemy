from pacote1 import modulo1
from pacote1 import modulo2
from pacote2 import modulo1 as modulo1_subtracao

print(type(modulo1))
print(modulo1.soma(2, 3))

modulo2.main()

print('Soma ', modulo1.soma(3, 2))
print('Subtração ', modulo1_subtracao.subtracao(3, 2))
