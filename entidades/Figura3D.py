from abc import ABC, abstractmethod


class Figura3D(ABC):

    @abstractmethod
    def calcularVolumen(self):
        pass

    @abstractmethod
    def calcularAreaSuperficial(self, factorEscalar):
        pass

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def getNombre(self):
        pass

    @abstractmethod
    def getAreaSuperficial(self):
        pass