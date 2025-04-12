from fastapi import APIRouter
from src.domain.dto.oferta_confirmar import ConfirmarOfertaRequestDTO, ConfirmarOfertaResponseDTO
from src.domain.dto.oferta_simular import SimularOfertaRequestDTO, SimularOfertasResponseDTO
from src.domain.use_cases.oferta_confirmar import ConfirmarOfertaUseCase
from src.domain.use_cases.oferta_simular import SimularOfertaUseCase
from src.database.repositories.produto_repository import ProdutoRepository
from src.resolver.bancarizador_resolver import get_bancarizador_adapter


router = APIRouter(prefix="/oferta")

@router.post("/simular", response_model=SimularOfertasResponseDTO) # Data Transfer Object
def simular_oferta(request: SimularOfertaRequestDTO):
    produto_config = ProdutoRepository().buscar_por_id(request.produto_id)
    bancarizador_adapter = get_bancarizador_adapter(produto_config.bancarizador)

    use_case = SimularOfertaUseCase(bancarizador_adapter)
    response_dto = use_case.execute(request)
    return response_dto

@router.post("/confirmar", response_model=ConfirmarOfertaResponseDTO)
def confirmar_oferta(request: ConfirmarOfertaRequestDTO):
    produto_config = ProdutoRepository().buscar_produto_por_authorization()
    bancarizador_adapter = get_bancarizador_adapter(produto_config.bancarizador)

    use_case = ConfirmarOfertaUseCase(bancarizador_adapter)
    response_dto = use_case.confirmar_oferta(request.id_oferta)
    return response_dto
