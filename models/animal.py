from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula):
        self.periodo_gestacion = periodo_gestacion
        self.region_procedencia = region_procedencia
        self.nombre_comun = nombre_comun
        self.nombre_cientifico = nombre_cientifico
        self.jaula = jaula
    
    @abstractmethod
    def alimentarse(self):
        pass

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass
        
        