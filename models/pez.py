from animal import Animal


class Pez(Animal):
    __cantidad_peces = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula)
        Pez.__cantidad_peces += 1

    def alimentarse(self):
        return "Los peces se alimentan de otros peces, crustáceos, plancton y algas."

    def hacer_sonido(self):
        return "Los peces no hacen sonidos."

    def moverse(self):
        return "Los peces se desplazan nadando."

    def __del__(self):
        Pez.__cantidad_peces -= 1