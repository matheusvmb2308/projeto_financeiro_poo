from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
class TestLancamento:
    def setup_method(self) -> None:
        self.cat = Categoria("Alimentação")
    def teste_cria_lancamento(self) -> None:
        lanc = Lancamento("Marmita", 10, "10/10/2026", self.cat)
        assert lanc.descricao == "Marmita"
        assert lanc.valor == 10
        assert lanc.data == "10/10/2026"
        assert lanc.categoria == self.cat
    def test_alterar_categoria_invalida(self) -> None:
        lanc = Lancamento("Marmita", 10, "10/10/2026", self.cat)
        try:
            lanc.alterarCategoria("Transporte")
            assert False, "Deve dar erro!"
        except TypeError:
            pass
    def teste_alterar_categoria_valida(self) -> None:
        lanc = Lancamento("Marmita", 10, "10/10/2026", self.cat)
        nova_cat = Categoria("Transporte")
        lanc.alterarCategoria(nova_cat)
        assert lanc.categoria == nova_cat