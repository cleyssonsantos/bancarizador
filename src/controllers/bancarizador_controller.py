from fastapi import APIRouter
from src.domain.dto.oferta_dto import SimularOfertaRequestDTO, SimularOfertasResponseDTO
from src.domain.use_cases.simular_oferta import SimularOfertaUseCase
from src.infrastructure.repositories.produto_repository import ProdutoRepository
from src.infrastructure.resolver.bancarizador_resolver import get_bancarizador_adapter


router = APIRouter()

@router.post("/oferta/simular", response_model=SimularOfertasResponseDTO) # Data Transfer Object
def simular_oferta(request: SimularOfertaRequestDTO):
    produto_config = ProdutoRepository().buscar_por_id(request.produto_id)
    bancarizador_adapter = get_bancarizador_adapter(produto_config.bancarizador)

    use_case = SimularOfertaUseCase(bancarizador_adapter)
    response_dto = use_case.execute(request)
    return response_dto
