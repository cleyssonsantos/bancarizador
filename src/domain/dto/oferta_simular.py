from pydantic import BaseModel, Field
from decimal import Decimal


class SimularOfertaRequestDTO(BaseModel):
    produto_id: str = Field(..., description="ID do produto")
    valor: Decimal = Field(..., description="Valor de simulação. Ex: 1200.0")
    parcelas: int = Field(..., description="Número de parcelas")


class SimularOfertasResponseDTO(BaseModel):
    valor_parcela: Decimal
    taxa_efetiva: float


