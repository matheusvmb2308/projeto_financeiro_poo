from financeiro.categoria import Categoria
class TesteCategoria: 
    def teste_cria_categoria_com_nome(self) -> None:  
        cat = Categoria("Alimentação")
        assert cat.nome == "Alimentação"