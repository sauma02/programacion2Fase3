from Figura3D import Figura3D
import math

class Cilindro(Figura3D):
    """Representa un cilindro tridimensional."""

    def __init__(self, radio, altura):
        self.radio=radio;
        self.altura=altura;
        self.area=0;
        self.nombre="Cilindro";
        
    def calcularVolumen(self):
        #Calculamos el volumen del cilindro por la formula general pi*radio al cuadrado*altura
        return math.pi * self.radio ** 2 * self.altura
    
    def calcularAreaSuperficial(self, factorEscalar):
        #Calculamos el area superficial teniendo en cuenta formula general del area del cilindro y su constante, 2, dejamos el escalar como una variable asignada por el usuario para que pueda asignarlo
        radio = self.radio * factorEscalar;
        altura = self.altura * factorEscalar;
        self.area = 2 * math.pi * radio * (radio + altura);
        return self.area;
    
    def dibujar(self):
        return print(f"Cilindro de radio: {self.radio}"
                     f"y Altura: {self.altura}");
    def getNombre(self):
        return self.nombre;
    def getAreaSuperficial(self):
            return self.area;    
        
        
    