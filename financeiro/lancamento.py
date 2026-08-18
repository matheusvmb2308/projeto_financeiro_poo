from financeiro.categoria import Categoria
class Lancamento: 
    def __init__(self, descricao: str, valor: float, data: str, categoria: Categoria) -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria
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
        