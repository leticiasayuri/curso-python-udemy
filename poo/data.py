class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data1 = Data()
data1.dia = 5
data1.mes = 12
data1.ano = 2019
print(data1)

data2 = Data()
data2.dia = 7
data2.mes = 11
data2.ano = 2020
print(data2)
