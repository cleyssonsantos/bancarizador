from unittest.mock import Mock
from src.domain.dto.oferta_dto import SimularOfertaRequestDTO
from src.domain.use_cases.simular_oferta import SimularOfertaUseCase

def test_simulacao_unitaria_qitech():
    adapter_mock = Mock()
    adapter_mock.simular_oferta.return_value = {
        "valor_parcela": 120.50,
        "taxa": 1.99
    }
    input_dto = SimularOfertaRequestDTO(valor=1200.0, parcelas=12, produto_id="123194")
    response = SimularOfertaUseCase(adapter_mock).execute(input_dto)
    assert response.valor_parcela == 120.50
    assert response.taxa_efetiva == 1.99
    adapter_mock.simular_oferta.assert_called_once()
