from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adiciona(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procura(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def conclui(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    tarefas_casa = Projeto('Tarefas de Casa')
    tarefas_casa.adiciona('Passar roupa')
    tarefas_casa.adiciona('Lavar prato')
    print(tarefas_casa)

    tarefas_casa.procura('Lavar prato').conclui()
    for tarefa in tarefas_casa.tarefas:
        print(f'- {tarefa}')

    print(tarefas_casa)

    tarefas_mercado = Projeto('Compras no mercado')
    tarefas_mercado.adiciona('Frutas secas')
    tarefas_mercado.adiciona('Carne')
    tarefas_mercado.adiciona('Tomate')
    print(tarefas_mercado)

    comprar_carne = tarefas_mercado.procura('Carne')
    comprar_carne.conclui()

    for tarefa in tarefas_mercado.tarefas:
        print(f'- {tarefa}')
    print(tarefas_mercado)


if __name__ == '__main__':
    main()
