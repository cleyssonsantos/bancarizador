from src.domain.dto.oferta_dto import SimularOfertaRequestDTO, SimularOfertasResponseDTO
from src.domain.models.oferta import Oferta
from src.domain.ports.bancarizador_port import BancarizadorPort


class SimularOfertaUseCase:
    def __init__(self, adapter: BancarizadorPort):
        self.adapter = adapter
    
    def execute(self, request_dto: SimularOfertaRequestDTO) -> SimularOfertasResponseDTO:
        oferta = Oferta(valor=request_dto.valor, parcelas=request_dto.parcelas)
        resultado = self.adapter.simular_oferta(oferta)

        return SimularOfertasResponseDTO(
            valor_parcela=resultado["valor_parcela"],
            taxa_efetiva=resultado["taxa"]
        )
