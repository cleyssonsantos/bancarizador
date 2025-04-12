class Produto:
    def __init__(self, id: str, bancarizador: str):
        self.id = id
        self.bancarizador = bancarizador

class ProdutoRepository:
    def buscar_por_id(self, produto_id: str) -> Produto:
        # Simula busca no banco
        return Produto(id=produto_id, bancarizador="qitech")

    def buscar_produto_por_authorization(self) -> Produto:
        # simula busca por auth
        return Produto(bancarizador="qitech", id="123")
