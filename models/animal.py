from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad):
        self.periodo_gestacion = periodo_gestacion
        self.region_procedencia = region_procedencia
        self._nombre_comun = nombre_comun
        self.nombre_cientifico = nombre_cientifico
        self.jaula = jaula
        self._cantidad = cantidad
    
    @abstractmethod
    def hacer_sonido(self):
        pass

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
            
    @property
    def nombre_comun(self):
        return self._nombre_comun

    @nombre_comun.setter
    def nombre_comun(self, nombre):
        if isinstance(nombre, str):
            self._nombre_comun = nombre.lower()

    def __str__(self):
        return f"Nombre común: {self.nombre_comun}\nNombre científico: {self.nombre_cientifico}\n" \
            f"Periodo de gestación: {self.periodo_gestacion} días\nRegión de procedencia: {self.region_procedencia}\n" \
            f"Jaula: {self.jaula}"
        
        