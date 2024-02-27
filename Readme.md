# Control de Animales en el Zoológico

Este proyecto de Python proporciona una aplicación de consola para el control de una lista de animales en un zoológico. La aplicación está orientada a objetos y permite realizar operaciones como buscar, crear, editar y eliminar animales en la lista.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `models/*`: Contiene las clases `Zoo`, `Animal`, `Mamifero`, `Reptil`, `Ave`, `Pez` y `ZooMenu` con sus respectivos modulos.
- `main.py`: Script principal para ejecutar la aplicación.

## Uso

Para ejecutar la aplicación, simplemente ejecuta `main.py`:

```bash
python main.py

Funcionalidades
Mostrar todos los animales: Muestra información detallada de todos los animales en el zoológico.

Buscar un animal: Busca un animal por su nombre común y muestra sus detalles.

Agregar un nuevo animal: Permite agregar un nuevo animal al zoológico, especificando el tipo (mamífero, reptil, ave, pez).

Actualizar información de un animal: Permite actualizar la información de un animal existente.

Eliminar un animal: Elimina un animal del zoológico.

Salir: Cierra la aplicación.

Requisitos
Python 3.*