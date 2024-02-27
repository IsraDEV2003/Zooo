from .AnimalManager import AnimalManager
from .validaciones import Validaciones
from .mamifero import Mamifero
from .ave import Ave
from .pez import Pez
from .reptil import Reptil




class ZooMenu:

    def __init__(self):
        self.zoo = AnimalManager()

    def mostrar_menu(self):
        print(  """
                    Bienvenido
                """)
        print("1. Mostrar todos los animales")
        print("2. Buscar un animal")
        print("3. Agregar un nuevo animal")
        print("4. Actualizar información de un animal")
        print("5. Eliminar un animal")
        print("6. Salir\n" )

    def ejecutar_menu(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.zoo.mostrar_todos()
            elif opcion == "2":
                self.buscar_animal()
            elif opcion == "3":
                self.agregar_nuevo_animal()
            elif opcion == "4":
                self.actualizar_informacion_animal()
            elif opcion == "5":
                self.eliminar_animal()
            elif opcion == "6":
                print("Hasta luego. ¡Gracias por visitar el Zoológico!")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 6.\n")

    def buscar_animal(self):
        nombre_busqueda = input("Ingrese el nombre del animal a buscar: ")
        animal_encontrado = self.zoo.buscar(nombre_busqueda)
        if animal_encontrado:
            print(animal_encontrado)
        else:
            print("Animal no encontrado.")

    def agregar_nuevo_animal(self):
        print("\n\nSeleccione el tipo de animal:")
        print("1. Mamífero")
        print("2. Reptil")
        print("3. Ave")
        print("4. Pez")
        tipo_animal = input("\n\nIngrese el número correspondiente al tipo de animal: ")

        nombre_comun = input("Ingrese el nombre común del animal: ")
        nombre_cientifico = input("Ingrese el nombre científico del animal: ")
        periodo_gestacion = 0
        region_procedencia = input("Ingrese la región de procedencia del animal: ")
        jaula = input("Ingrese la jaula del animal: ")
        cantidad = 0

        
        cantidad = Validaciones.obtener_cantidad_validada("Cantidad de animales: ")

        periodo_gestacion = Validaciones.obtener_cantidad_validada("Periodo de gestación: ")


        if tipo_animal == "1":
            nuevo_animal = Mamifero(periodo_gestacion,  region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)
        elif tipo_animal == "2":
            nuevo_animal = Reptil(periodo_gestacion,  region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)
        elif tipo_animal == "3":
            nuevo_animal = Ave(periodo_gestacion,  region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)
        elif tipo_animal == "4":
            nuevo_animal = Pez(periodo_gestacion,  region_procedencia, nombre_comun, nombre_cientifico, jaula, cantidad)
        else:
            print("Opción no válida. No se pudo agregar el animal.")
            return

        self.zoo.crear(nuevo_animal)
        print("Animal agregado al zoológico.")

    def actualizar_informacion_animal(self):

        nombre = input("Ingrese el nombre del animal a actualizar: ")
        propiedades = {}
        propiedades["nombre_comun"] = input("Nuevo nombre común: ")
        propiedades["nombre_cientifico"] = input("Nuevo nombre científico: ")
        propiedades["region_procedencia"] = input("Nueva región de procedencia: ")
        propiedades["jaula"] = input("Nueva jaula: ")

        propiedades["cantidad"] = Validaciones.obtener_cantidad_validada("Nueva cantidad de animales: ")
        propiedades["periodo_gestacion"] = Validaciones.obtener_cantidad_validada("Nuevo periodo de gestación: ")


        propiedades = {key: value for key, value in propiedades.items() if value != ""}

        self.zoo.editar(nombre, propiedades)
        print("Información del animal actualizada.")

    def eliminar_animal(self):
        nombre = input("Ingrese el nombre del animal a eliminar: ")
        self.zoo.eliminar(nombre)
        print("Animal eliminado del zoológico.")
