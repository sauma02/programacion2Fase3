from entidades.Figura3D import Figura3D
import math


class Esfera(Figura3D):

    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.nombre = "Esfera"

    def calcularVolumen(self):
        # 4/3 * pi * radio^3
        return 4 / 3 * math.pi * self.radio ** 3

    def calcularAreaSuperficial(self, factorEscalar):
        # 4 * pi * radio^2, con el radio escalado
        radio = self.radio * factorEscalar
        self.area = 4 * math.pi * radio ** 2
        return self.area

    def dibujar(self):
        return f"Esfera de radio: {self.radio}"

    def getNombre(self):
        return self.nombre

    def getAreaSuperficial(self):
        return self.area