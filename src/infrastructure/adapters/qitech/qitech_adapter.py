from src.domain.ports.bancarizador_port import BancarizadorPort
from src.domain.models.oferta import Oferta
from .qitech_client import QitechClient


class QitechAdapter(BancarizadorPort):
    def __init__(self):
        self.client = QitechClient()

    def simular_oferta(self, oferta: Oferta) -> dict:
        response = self.client.simular({
            "valor": str(oferta.valor), # Simulação de adaptação ao usar a rota da qitech
            "parcelas": oferta.parcelas
        })
        return {
            "valor_parcela": response["installment_amount"],
            "taxa": response["effective_rate"]
        }
