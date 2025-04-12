from abc import ABC, abstractmethod
from src.domain.models.oferta import Oferta


class BancarizadorPort(ABC):
    @abstractmethod
    def simular_oferta(self, oferta: Oferta) -> dict:
        pass
