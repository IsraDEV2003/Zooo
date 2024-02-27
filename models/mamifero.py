from .animal import Animal


class Mamifero(Animal):
    __cantidad_mamiferos = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)

    def hacer_sonido(self):
        return "Hace un sonido de mamífero."
    
    def __del__(self):
        Mamifero.__cantidad_mamiferos -= 1