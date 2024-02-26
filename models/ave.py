from animal import Animal


class Ave(Animal):
    __cantidad_aves = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula)
        Ave.__cantidad_aves += 1

    def alimentarse(self):
        return "Las aves se alimentan de insectos, frutas, semillas y otros animales."

    def hacer_sonido(self):
        return "Las aves hacen sonidos variados."

    def moverse(self):
        return "Las aves se desplazan volando."

    def __del__(self):
        Ave.__cantidad_aves -= 1