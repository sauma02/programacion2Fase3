from entidades.Figura3D import Figura3D


class Cubo(Figura3D):

    def __init__(self, lado):
        self.lado = lado
        self.area = 0
        self.nombre = "Cubo"

    def calcularVolumen(self):
        # Volumen del cubo: lado al cubo
        return self.lado ** 3

    def calcularAreaSuperficial(self, factorEscalar):
        # 6 caras; el factor escalar lo define el usuario
        ladoEscalado = self.lado * factorEscalar
        self.area = 6 * ladoEscalado ** 2
        return self.area

    def dibujar(self):
        return f"Cubo de lados: {self.lado}"

    def getNombre(self):
        return self.nombre

    def getAreaSuperficial(self):
        return self.area