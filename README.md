# Sistema de Gestión de Biblioteca

Este proyecto para la materia de Estructuras de Datos implementa un sistema para la gestión de libros, usuarios y préstamos de una biblioteca.

## Estructuras de Datos Utilizadas

* **Listas:** Para almacenar el catálogo general de los libros.
* **Pilas:** Para el historial de últimas acciones.
* **Colas:** Para gestionar la cola de espera de préstamos de libros agotados.
* **Árboles binarios de búsqueda:** Para realizar búsquedas eficientes de libros por ISBN o Título.

## Integrantes del equipo

* **Carol Dayanna Guzmán Gómez** (carol.guzmango@amigo.edu.co) - [@carolguzmango-cloud](https://github.com/carolguzmango-cloud)
* **Valentina Posada Cadavid** (valentina.posadaad@amigo.edu.co) - [@valep7](https://github.com/valep7)
* **María Camila Bustamante Gutiérrez** (maria.bustamantegu@amigo.edu.co) - [@mariabustamantegu-jpg](https://github.com/mariabustamantegu-jpg)

## Establecer estructura inicial del sistema de biblioteca

* **Definir registro y consulta de libros y usuarios**
* **Planificar gestión de préstamos y devoluciones**
* **Establecer control de solicitudes mediante estructuras de datos**
* **Crear estructura y planificación inicial del proyecto**

## Planificar estructuras de datos del sistema

* **Analizar el uso de listas, pilas y colas**
* **Definir árbol binario de búsqueda para libros**
* **Establecer la función de cada estructura dentro del sistema**
* **Organizar la base conceptual para la implementación**
  ## Primer avance del proyecto
  (se realiza un modelo relacional para establecer tablas y cardinalidad, se empezaron a hacer en consola neon )
  
biblioteca.py
#sistema de gestión de biblioteca
print("sistema de biblioteca")
print("Bienvenido al sistema de gestión de préstamos")
print("opciones: ")
print("1. Registrar libro")
print("2. Mostrar libros")
print("3. Prestar libro")
print("4. Devolver libro")
print("5. Buscar libro")
print("0. salir")
#inicio del sistema biblioteca 
