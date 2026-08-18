from financeiro.categoria import Categoria
class Lancamento: 
    def __init__(self, descricao: str, valor: float, data: str, categoria: Categoria) -> None:
        self_descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria