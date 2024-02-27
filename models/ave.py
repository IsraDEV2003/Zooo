from .animal import Animal


class Ave(Animal):
    __cantidad_aves = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)
        Ave.__cantidad_aves += 1

    def hacer_sonido(self):
        return "Hace un sonido de ave."

    def __del__(self):
        Ave.__cantidad_aves -= 1