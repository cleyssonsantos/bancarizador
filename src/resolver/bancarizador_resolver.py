from src.adapters.qitech.qitech_adapter import QitechAdapter
from enum import Enum


class Bancarizadores(Enum):
    QITECH = "qitech"


ADAPTERS = {
    Bancarizadores.QITECH: QitechAdapter,
}

def get_bancarizador_adapter(nome: str):
    try:
        nome_enum = Bancarizadores(nome)
        return ADAPTERS[nome_enum]()
    except ValueError:
        raise ValueError(f"Bancarizador '{nome}' não suportado")
