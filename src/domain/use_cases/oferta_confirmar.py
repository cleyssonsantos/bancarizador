from src.domain.ports.bancarizador_port import BancarizadorPort


class ConfirmarOfertaUseCase:
    def __init__(self, adapter: BancarizadorPort):
        self.adapter = adapter

    def confirmar_oferta(self, id_oferta: int) -> dict:
        return {"mensagem": "Oferta confirmada", "id_oferta": id_oferta}
    
