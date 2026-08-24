from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.conciliacao import Conciliacao
 
 
class TestConciliacao:
    def setup_method(self) -> None:
        self.cat = Categoria("Geral")
        self.debito1 = Lancamento("Pagamento fornecedor", 150.0, "01/08/2026", self.cat)
        self.debito2 = Lancamento("Compra material", 50.0, "02/08/2026", self.cat)
        self.credito1 = Lancamento("Recebimento cliente", 100.0, "01/08/2026", self.cat)
        self.credito2 = Lancamento("Recebimento cliente 2", 100.0, "03/08/2026", self.cat)
 
    def teste_total_debitos(self) -> None:
        conciliacao = Conciliacao([self.debito1, self.debito2], [self.credito1, self.credito2])
        assert conciliacao.total_debitos() == 200.0
 
    def teste_total_creditos(self) -> None:
        conciliacao = Conciliacao([self.debito1, self.debito2], [self.credito1, self.credito2])
        assert conciliacao.total_creditos() == 200.0
 
    def teste_total_debitos_lista_vazia(self) -> None:
        conciliacao = Conciliacao([], [self.credito1])
        assert conciliacao.total_debitos() == 0.0
 
    def teste_total_creditos_lista_vazia(self) -> None:
        conciliacao = Conciliacao([self.debito1], [])
        assert conciliacao.total_creditos() == 0.0
 
    def teste_verifica_conciliacao_totais_iguais(self) -> None:
        conciliacao = Conciliacao([self.debito1], [self.credito1, self.debito2])
        assert conciliacao.verifica_conciliacao() is True
 
    def teste_verifica_conciliacao_totais_diferentes(self) -> None:
        conciliacao = Conciliacao([self.debito1, self.debito2], [self.credito1])
        assert conciliacao.verifica_conciliacao() is False
 
    def teste_verifica_conciliacao_ambas_vazias(self) -> None:
        conciliacao = Conciliacao([], [])
        assert conciliacao.verifica_conciliacao() is True
    def teste_adiciona_debito_sem_lista(self) -> None:
        try:
            conciliacao = Conciliacao(self.debito1, self.debito2)
            raise False
        except TypeError:
            pass