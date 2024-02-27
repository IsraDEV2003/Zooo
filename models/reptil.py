from .animal import Animal


class Reptil(Animal):
    __cantidad_reptiles = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)
        Reptil.__cantidad_reptiles += 1

    def hacer_sonido(self):
        return "Hace un sonido de reptil."

    def __del__(self):
        Reptil.__cantidad_reptiles -= 1

    