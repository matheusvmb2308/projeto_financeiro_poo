from financeiro.lancamento import Lancamento
class Fechamento:
    def __init__(self) -> None:
        self.fechamentos: list[Lancamento] = []
    def adicionarFechamento(self, fechamento: Lancamento) -> None:
        if not isinstance(fechamento, Lancamento):
            raise TypeError("Fechamento Inválido")
        self.fechamentos.append(fechamento)
    def removerFechamento(self, fechamento: Lancamento) -> None:
        self.fechamentos = [i for i in self.fechamentos if i.fechamento is not fechamento]
    def calculaTotal(self) -> float:
        return sum(self.valor for fechamento in self.fechamentos)