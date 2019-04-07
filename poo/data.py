class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data1 = Data(5, 12, 2019)
print(data1)

data2 = Data(7, 11, 2020)
print(data2)
