from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def conclui(self):
        self.feito = True

    def __str__(self):
        return self.descricao + ('(Concluída)' if self.feito else '')


def main():
    tarefas_casa = []
    tarefas_casa.append(Tarefa('Passar roupa'))
    tarefas_casa.append(Tarefa('Lavar prato'))

    [tarefa.conclui() for tarefa in tarefas_casa if tarefa.descricao == 'Lavar prato']
    for tarefa in tarefas_casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
