class Conciliacao:
    def __init__(self, debito, credito) -> None:
        self.debitos = [debito]
        self.creditos = [credito]
    def total_debitos(self) -> float:
        return sum(debito.valor for debito in self.debitos)
    def total_creditos(self) -> float:
        return sum(credito.valor for credito in self.creditos)
    def verifica_conciliacao(self) -> bool:
        return self.total_creditos() == self.total_debitos()
    
    