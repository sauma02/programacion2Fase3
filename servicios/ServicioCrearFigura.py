from entidades.Cubo import Cubo
from entidades.Cilindro import Cilindro
from entidades.Esfera import Esfera
from entidades.Figura3D import Figura3D


class ServicioCrearFigura:

    def __init__(self):
        self.lista = []

    def agregarFigura(self, figura):
        self.lista.append(figura)

    def crearCubo(self, lado, escalar):
        cubo = Cubo(lado)
        self.cambiarValorEscalar(cubo, escalar)
        self.agregarFigura(cubo)
        return cubo

    def crearCilindro(self, radio, altura, escalar):
        cilindro = Cilindro(radio, altura)
        self.cambiarValorEscalar(cilindro, escalar)
        self.agregarFigura(cilindro)
        return cilindro

    def crearEsfera(self, radio, escalar):
        esfera = Esfera(radio)
        self.cambiarValorEscalar(esfera, escalar)
        self.agregarFigura(esfera)
        return esfera

    def listarFigurasActuales(self):
        return self.lista

    def cambiarValorEscalar(self, figura: Figura3D, factorEscalar):
        return figura.calcularAreaSuperficial(factorEscalar)