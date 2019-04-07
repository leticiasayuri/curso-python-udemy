class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data1 = Data(5, 12, 2019)
print(data1)

data2 = Data(7, 11, 2020)
print(data2)

data3 = Data()
print(data3)

data4 = Data(ano=2022)
print(data4)
