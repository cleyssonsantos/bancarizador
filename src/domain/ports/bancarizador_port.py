from abc import ABC, abstractmethod
from src.domain.models.oferta import Oferta


class BancarizadorPort(ABC):
    @abstractmethod
    def simular_oferta(self, oferta: Oferta) -> dict:
        pass

    @abstractmethod
    def confirmar_oferta(self, id_oferta: int) -> dict:
        pass
