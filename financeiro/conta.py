class Conta: 
    def __init__(self, nome: str, saldo: float):
        self._nome = nome
        self._saldo = saldo
    def getNome(self) -> None:
        return self._nome
    def getSaldo(self) -> None:
        return self._saldo
    def alterarSaldo(self, novoSaldo) -> None:
        if novoSaldo <= 0:
            raise ValueError("Saldo deve ser maior que 0")
        self._saldo = novoSaldo
    def alterarNome(self, novoNome) -> None:
        if novoNome == "":
            raise ValueError("Nome não pode ser vazio!")
        self._nome = novoNome