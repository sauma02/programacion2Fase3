from Figura3D import Figura3D;
import math;

class Esfera(Figura3D):
    
    def __init__(self, radio):
        self.radio = radio;
        self.area= 0;
        self.nombre="Esfera";
        
    def calcularVolumen(self):
        #Calculamos el volumen de la esfera por la formula general 4/3*pi*radio al cubo
        return 4/3 * math.pi * self.radio ** 3
    
    def calcularAreaSuperficial(self, factorEscalar):
        #Calculamos el area superficial teniendo en cuenta formula general del area de la esfera y su constante, 4, dejamos el escalar como una variable asignada por el usuario para que pueda asignarlo
        radio = self.radio * factorEscalar;
        self.area= 4 * math.pi * radio ** 2;
        return self.area;
    
    def dibujar(self):
        return print(f"Esfera de radio: {self.radio}");
    
    def getNombre(self):
        return self.nombre;
    def getAreaSuperficial(self):
        return self.area;
        