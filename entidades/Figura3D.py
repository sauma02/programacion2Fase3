from abc import ABC, abstractmethod;
import math;

class Figura3D(ABC):
    
    @abstractmethod
    def calcularVolumen(self):
        pass;
        
    @abstractmethod
    def calcularAreaSuperficial(self, factorEscalar):
        pass;
    
    
    @abstractmethod
    def dibujar(self):
        pass;