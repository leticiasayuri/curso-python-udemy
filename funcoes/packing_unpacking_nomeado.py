# **kwargs
def resultado_f1_packing(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


def resultado_f1_unpacking(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    resultado_f1_packing(primeiro='L. Hamilton',
                         segundo='M. Verstappen',
                         terceiro='S. Vettel')

    podium = {'segundo': 'M. Verstappen',
              'primeiro': 'L. Hamilton',
              'terceiro': 'S. Vettel'}
    resultado_f1_unpacking(**podium)
