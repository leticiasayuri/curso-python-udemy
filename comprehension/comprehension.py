# [ expressão for item in list ]
print('List Comprehension sem condição')
dobros = [i * 2 for i in range(10)]
print(dobros)

# Versão "normal"
print('\nVersão "normal"')
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)

# [ expressão for item in list if condicional ]
print('\nList Comprehension com condição')
dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_dos_pares)

# Versão "normal"
print('\nVersão "normal"')
dobros_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)
print(dobros_dos_pares)

print('\nGenerator')
generator = (i ** 2 for i in range(10) if i % 2 == 0)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for numero in generator:
    print(numero)

print('\nDicionário')
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
