from abc import ABC

class Validaciones(ABC):

    @staticmethod
    def validar_numero_no_negativo(valor):
        try:
            numero = int(valor)
            if numero < 0:
                print(f"\nAdvertencia: debe ser un número no negativo.")
                return None
            return numero
        except ValueError:
            print(f"\nAdvertencia: debe ser un número entero no negativo.")
            return None
        
    @staticmethod
    def obtener_cantidad_validada(pregunta: str):
        while True:
            cantidad = input(pregunta)
            cantidad_validada = Validaciones.validar_numero_no_negativo(cantidad)
            if cantidad_validada is not None:
                return cantidad_validada