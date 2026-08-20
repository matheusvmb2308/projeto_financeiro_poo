from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento

class TestFechamento:
    def setup_method(self) -> None:
        self.cat = Categoria("Alimentação")
        self.lancamento = Lancamento("Marmita", 10, "10/10/2026", self.cat)
    def teste_adiciona_fechamento(self) -> None:
        fechamento = Fechamento()
        fechamento.adicionarLancamento(self.lancamento)
        assert fechamento.lancamentos[0] == self.lancamento
    def teste_remove_fechamento(self) -> None:
        fechamento = Fechamento()
        fechamento.adicionarLancamento(self.lancamento)
        fechamento.removerLancamento(self.lancamento)
        assert len(fechamento.lancamentos) == 0
    def teste_calculo_total(self) -> None:
        fechamento = Fechamento()
        fechamento.adicionarLancamento(self.lancamento)
        fechamento.adicionarLancamento(self.lancamento)
        assert fechamento.calculaTotal() == 20
    def teste_fechamento_vazio(self) -> None:
        fechamento = Fechamento()
        assert fechamento.quantidade_lancamentos() == 0
        assert fechamento.calculaTotal() == 0.0
        