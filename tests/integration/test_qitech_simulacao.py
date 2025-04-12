from src.infrastructure.adapters.qitech.qitech_adapter import QitechAdapter
from src.domain.dto.oferta_dto import SimularOfertaRequestDTO

def test_qitech_adapter():
    adapter = QitechAdapter()
    input_dto = SimularOfertaRequestDTO(valor=1000, parcelas=12, produto_id="128417")
    resultado = adapter.simular_oferta(input_dto)
    assert resultado["valor_parcela"] >= resultado["taxa"]
