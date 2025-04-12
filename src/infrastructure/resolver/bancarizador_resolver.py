from src.infrastructure.adapters.qitech.qitech_adapter import QitechAdapter


def get_bancarizador_adapter(nome: str):
    match nome:
        case "qitech":
            return QitechAdapter()
        case "teste":
            return None #Teste()
        case _:
            raise ValueError("Bancarizador não suportado")
