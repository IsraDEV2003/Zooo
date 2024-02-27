from .animal import Animal

class AnimalManager:
    def __init__(self) -> None:
        self.animales = []
    
    def crear(self, animal:Animal):
        for dato in self.animales:
            if dato.nombre_comun is animal.nombre_comun:
                dato.cantidad += animal.cantidad
                return True
        self.animales.append(animal)
        return True    
        
    def buscar(self, nombre:str):
        for animal in self.animales:
            if nombre.lower() == animal.nombre_comun:
                return animal
        return None

    
    def editar(self, nombre, propiedades):
        animal = self.buscar(nombre)

        if animal:
            if "nombre_comun" in propiedades:
                animal.nombre_comun = propiedades["nombre_comun"]
            if "nombre_cientifico" in propiedades:
                animal.nombre_cientifico = propiedades["nombre_cientifico"]
            if "periodo_gestacion" in propiedades:
                animal.periodo_gestacion = propiedades["periodo_gestacion"]
            if "region_procedencia" in propiedades:
                animal.region_procedencia = propiedades["region_procedencia"]
            if "jaula" in propiedades:
                animal.jaula = propiedades["jaula"]
            if "cantidad" in propiedades:
                animal.cantidad = propiedades["cantidad"]

    def eliminar(self, nombre: str) -> bool:
        animal = self.buscar(nombre)
        if animal:
            self.animales.remove(animal)
            return True
        return False
    
    def mostrar_todos(self):
        for animal in self.animales:
            print(animal)
