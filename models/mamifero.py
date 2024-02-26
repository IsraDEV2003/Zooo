from animal import Animal


class Mamifero(Animal):
    __cantidad_mamiferos = 0

    def __init__(self, periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula):
        super().__init__(periodo_gestacion, region_procedencia, nombre_comun, nombre_cientifico, jaula)

    def alimentarse(self):
        return "Los mamíferos se alimentan de leche materna, frutas, vegetales y carne."
    
    def hacer_sonido(self):
        return "Los mamíferos hacen sonidos variados."
    
    def moverse(self):
        return "Los mamíferos se desplazan caminando, corriendo, saltando o nadando."
    
    def __del__(self):
        Mamifero.__cantidad_mamiferos -= 1