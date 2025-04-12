from pydantic import BaseModel

class ConfirmarOfertaRequestDTO(BaseModel):
    id_oferta: int


class ConfirmarOfertaResponseDTO(BaseModel):
    id_oferta: int
    mensagem: str
