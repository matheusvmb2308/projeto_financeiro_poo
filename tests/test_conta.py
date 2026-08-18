from financeiro.conta import Conta
class TesteConta:
    def teste_cria_conta(self) -> None:
        conta = Conta("Matheus", 2500.0)
        assert conta.getNome() == "Matheus"
    def teste_alterar_saldo(self) -> None:
        conta = Conta("Josué", 5000.0)
        conta.alterarSaldo(6000.0)
        assert conta.getSaldo() == 6000
    def teste_alterar_nome(self) ->None:
        conta = Conta("Matheus", 0)
        conta.alterarNome("Josué")
        assert conta.getNome() == "Josué"
    def teste_altera_nome_invalido(self) -> None:
        c = Conta("Matheus", 2000.0)
        try:
            c.alterarNome("")
            assert False, "Não pode!"
        except ValueError:
            pass