from Figura3D import Figura3D;
import math;

class Cubo(Figura3D):
   
    def __init__(self, lado):
        self.lado=lado;
        self.nombre="Cubo";
    
    def calcularVolumen(self):
        #Calculamos el volumen del cuadrado, que seria su lado al cubo
        return self.lado ** 3;  
    
    def calcularAreaSuperficial(self, factorEscalar):
        #Calculamos el area superficial teniendo en cuenta la cantidad de caras con las que cuenta el cubo, 6, dejamos el escalar como una variable asignada por el usuario para que pueda asignarlo
        ladoEscalado = self.lado * factorEscalar;
        self.area= 6 * ladoEscalado ** 2;
        return self.area;  
    def dibujar(self):
        return print(f"Cubo de lados: {self.lado}");
    
    def getNombre(self):
        return self.nombre;
    def getAreaSuperficial(self):
            return self.area;
    
    