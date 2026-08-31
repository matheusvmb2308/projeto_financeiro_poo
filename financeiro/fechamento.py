from financeiro.lancamento import Lancamento
from financeiro.categoria import Categoria
class Fechamento:
    def __init__(self) -> None:
        self.lancamentos: list[Lancamento] = []
    def getFechamentos(self) -> list[Lancamento]:
        return list(self.lancamentos)
    def adicionarLancamento(self, lancamento: Lancamento) -> None:
        if not isinstance(lancamento, Lancamento):
            raise TypeError("Fechamento Inválido")
        self.lancamentos.append(lancamento)
    def removerLancamento(self, lancamento: Lancamento) -> None:
        if not isinstance(lancamento, Lancamento) or lancamento == None:
            raise TypeError("Lancamento Inválido")
        self.lancamentos = [i for i in self.lancamentos if i is not lancamento]
    def calculaTotal(self) -> float:
        return sum(lancamento.valor for lancamento in self.lancamentos)
    def quantidade_lancamentos(self) -> int:
        return len(self.lancamentos)
if __name__ == "__main__":
    cat = Categoria("Alimentação")
    lan = Lancamento("Marmita", 10, "10/10/2026", cat)
    fechamento = Fechamento()
    fechamento.adicionarLancamento(lan)
    fechamento.adicionarLancamento(lan)
    print(fechamento.getFechamentos())