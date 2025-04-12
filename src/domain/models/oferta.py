from pydantic import BaseModel
from decimal import Decimal


class Oferta(BaseModel):
    valor: Decimal
    parcelas: int
