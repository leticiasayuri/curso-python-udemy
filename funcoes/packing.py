def soma_dois(a, b):
    return a + b


def soma_tres(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_dois(2, 3))
    print(soma_tres(2, 4, 6))

    # Packing
    # Empacotamento dos argumentos em uma tupla para serem passados a função
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))

    # Unpacking
    # Desempacotamento de uma tupla/lista para os argumentos serem passados a função
    tupla_nums = (1, 2, 3)
    print(soma_tres(*tupla_nums))

    lista_nums = [1, 2, 3]
    print(soma_tres(*lista_nums))
