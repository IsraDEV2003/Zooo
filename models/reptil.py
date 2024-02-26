from animal import Animal


class Reptil(Animal):
    __cantidad_reptiles = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula)
        Reptil.__cantidad_reptiles += 1

    def alimentarse(self):
        return "Los reptiles se alimentan de insectos, frutas, vegetales y otros reptiles."
    
    def hacer_sonido(self):
        return "Los reptiles no hacen sonidos."
    
    def moverse(self):
        return "Los reptiles se desplazan arrastrándose."
    
    def __del__(self):
        Reptil.__cantidad_reptiles -= 1