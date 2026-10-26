from entidades.Figura3D import Figura3D
import math


class Cilindro(Figura3D):
    """Representa un cilindro tridimensional."""

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        self.area = 0
        self.nombre = "Cilindro"

    def calcularVolumen(self):
        # pi * radio^2 * altura
        return math.pi * self.radio ** 2 * self.altura

    def calcularAreaSuperficial(self, factorEscalar):
        # 2 * pi * r * (r + h), con radio y altura escalados
        radio = self.radio * factorEscalar
        altura = self.altura * factorEscalar
        self.area = 2 * math.pi * radio * (radio + altura)
        return self.area

    def dibujar(self):
        return f"Cilindro de radio: {self.radio} y altura: {self.altura}"

    def getNombre(self):
        return self.nombre

    def getAreaSuperficial(self):
        return self.area