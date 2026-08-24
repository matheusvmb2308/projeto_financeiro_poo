from financeiro.categoria import Categoria
class Lancamento: 
    def __init__(self, descricao: str, valor: float, data: str, categoria: Categoria, tipo: str = "credito") -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria
        if tipo not in ("debito","credito"):
            raise ValueError("Tipo deve ser debito ou crédito")
        self.tipo = tipo
    def alterarValor(self, novoValor) -> None:
        if novoValor <= 0:
            raise ValueError("Valor abaixo de 0")
        self.valor = novoValor
    def alterarCategoria(self, novaCategoria: Categoria) -> None:
        if not isinstance(novaCategoria, Categoria):
            raise TypeError("Categoria Inválida!")
        self.categoria = novaCategoria
    def alterarData(self, novaData) -> None:
        self.data = novaData
    def __repr__(self) -> str:
        return f"Lançamento: {self.descricao}"    