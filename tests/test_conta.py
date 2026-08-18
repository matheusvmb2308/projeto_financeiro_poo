from financeiro.conta import Conta
class TesteConta:
    def teste_cria_conta(self) -> None:
        conta = Conta("Matheus", 2500.0)
        assert conta.getNome() == "Matheus"