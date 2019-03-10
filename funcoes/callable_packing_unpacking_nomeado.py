def calcula_preco_final(preco_bruto, calcula_imposto, **params):
    return preco_bruto + preco_bruto * calcula_imposto(**params)


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_multiplicacao=1):
    return 0.11 * fator_multiplicacao if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calcula_preco_final(preco_bruto, imposto_x, importado=True)
    preco_final = calcula_preco_final(
        preco_final, imposto_y, explosivo=True, fator_multiplicacao=1.5)
    print(f'Preço final R$ {preco_final}')
