from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento
from financeiro.extrato import Extrato


class TestExtrato:
    def setup_method(self) -> None:
        self.cat = Categoria("Geral")

        # lançamentos dentro do período (08/2026)
        self.debito1 = Lancamento("Pagamento fornecedor", 150.0, "01/08/2026", self.cat, tipo="debito")
        self.debito2 = Lancamento("Compra material", 50.0, "15/08/2026", self.cat, tipo="debito")
        self.credito1 = Lancamento("Recebimento cliente", 100.0, "02/08/2026", self.cat, tipo="credito")
        self.credito2 = Lancamento("Recebimento cliente 2", 100.0, "20/08/2026", self.cat, tipo="credito")

        # lançamento fora do período (deve ser ignorado)
        self.lancamento_fora = Lancamento("Compra setembro", 999.0, "05/09/2026", self.cat, tipo="debito")

        self.fechamento = Fechamento()
        for lancamento in (self.debito1, self.debito2, self.credito1, self.credito2, self.lancamento_fora):
            self.fechamento.adicionarLancamento(lancamento)

    def teste_cria_extrato_com_mes_e_ano(self) -> None:
        extrato = Extrato(8, 2026)
        assert extrato.mes == 8
        assert extrato.ano == 2026

    def teste_mes_invalido_gera_erro(self) -> None:
        try:
            Extrato(13, 2026)
            assert False, "Deveria dar erro para mês inválido"
        except ValueError:
            pass

    def teste_adiciona_fechamento_invalido(self) -> None:
        extrato = Extrato(8, 2026)
        try:
            extrato.adicionarFechamento("não é um fechamento")
            assert False, "Deveria dar erro"
        except TypeError:
            pass

    def teste_total_lancamentos_ignora_fora_do_periodo(self) -> None:
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        assert extrato.total_lancamentos() == 4

    def teste_total_debitos(self) -> None:
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        assert extrato.total_debitos() == 200.0

    def teste_total_creditos(self) -> None:
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        assert extrato.total_creditos() == 200.0

    def teste_saldo_final(self) -> None:
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        assert extrato.saldo_final() == 0.0

    def teste_saldo_final_negativo_quando_debitos_maiores(self) -> None:
        fechamento = Fechamento()
        fechamento.adicionarLancamento(Lancamento("Aluguel", 300.0, "10/08/2026", self.cat, tipo="debito"))
        fechamento.adicionarLancamento(Lancamento("Salário", 100.0, "05/08/2026", self.cat, tipo="credito"))
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(fechamento)
        assert extrato.saldo_final() == -200.0

    def teste_extrato_sem_fechamentos_fica_zerado(self) -> None:
        extrato = Extrato(8, 2026)
        assert extrato.total_lancamentos() == 0
        assert extrato.total_debitos() == 0.0
        assert extrato.total_creditos() == 0.0
        assert extrato.saldo_final() == 0.0

    def teste_conciliacao_ok_quando_totais_batem(self) -> None:
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        assert extrato.possui_conciliacao_pendente() is False

    def teste_conciliacao_pendente_quando_totais_nao_batem(self) -> None:
        fechamento = Fechamento()
        fechamento.adicionarLancamento(Lancamento("Compra", 80.0, "10/08/2026", self.cat, tipo="debito"))
        fechamento.adicionarLancamento(Lancamento("Recebimento", 50.0, "12/08/2026", self.cat, tipo="credito"))
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(fechamento)
        assert extrato.possui_conciliacao_pendente() is True

    def teste_conciliacao_sem_lancamentos_nao_fica_pendente(self) -> None:
        extrato = Extrato(8, 2026)
        assert extrato.possui_conciliacao_pendente() is False

    def teste_agrega_varios_fechamentos_do_mesmo_periodo(self) -> None:
        fechamento2 = Fechamento()
        fechamento2.adicionarLancamento(Lancamento("Recebimento extra", 30.0, "22/08/2026", self.cat, tipo="credito"))

        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        extrato.adicionarFechamento(fechamento2)

        assert extrato.total_lancamentos() == 5
        assert extrato.total_creditos() == 230.0

    def teste_resumo_retorna_dict_com_os_dados_esperados(self) -> None:
        extrato = Extrato(8, 2026)
        extrato.adicionarFechamento(self.fechamento)
        resumo = extrato.resumo()
        assert resumo == {
            "periodo": "08/2026",
            "total_lancamentos": 4,
            "total_debitos": 200.0,
            "total_creditos": 200.0,
            "saldo_final": 0.0,
            "conciliacao_pendente": False,
        }