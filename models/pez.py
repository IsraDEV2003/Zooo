from .animal import Animal


class Pez(Animal):
    __cantidad_peces = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula,  cantidad):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula,  cantidad)
        Pez.__cantidad_peces += 1

    def hacer_sonido(self):
        return "Los peces no hacen sonidos."

    def __del__(self):
        Pez.__cantidad_peces -= 1