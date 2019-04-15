from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def _adiciona_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _adiciona_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def adiciona(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._adiciona_tarefa if isinstance(
            tarefa, Tarefa) else self._adiciona_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procura(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def conclui(self):
        self.feito = True

    def __str__(self):
        status = []

        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def conclui(self):
        super().conclui()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    tarefas_casa = Projeto('Tarefas de Casa')
    tarefas_casa.adiciona('Passar roupa', datetime.now())
    tarefas_casa.adiciona('Lavar prato')
    tarefas_casa.adiciona(TarefaRecorrente(
        'Trocar lençóis', datetime.now(), 7))
    tarefas_casa.adiciona(tarefas_casa.procura('Trocar lençóis').conclui())
    print(tarefas_casa)

    tarefas_casa.procura('Lavar prato').conclui()
    for tarefa in tarefas_casa:
        print(f'- {tarefa}')

    print(tarefas_casa)

    tarefas_mercado = Projeto('Compras no mercado')
    tarefas_mercado.adiciona('Frutas secas')
    tarefas_mercado.adiciona('Carne')
    tarefas_mercado.adiciona('Tomate', datetime.now() +
                             timedelta(days=3, minutes=12))
    print(tarefas_mercado)

    comprar_carne = tarefas_mercado.procura('Carne')
    comprar_carne.conclui()

    for tarefa in tarefas_mercado:
        print(f'- {tarefa}')
    print(tarefas_mercado)


if __name__ == '__main__':
    main()
