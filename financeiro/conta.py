class Conta: 
    def __init__(self, nome: str, saldo: float):
        self._nome = nome
        self._saldo = saldo
    def getNome(self) -> None:
        return self._nome
    def getSaldo(self) -> None:
        return self._saldo