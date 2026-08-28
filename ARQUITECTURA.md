#  Arquitectura del Sistema de Biblioteca

##  Estructuras de Datos en Memoria RAM

El sistema utiliza dos estructuras fundamentales para la gestión de datos:

1. **Vector de Libros (Arreglo 1D):** Representa el catálogo contiguo de libros.
2. **Matriz de Préstamos (Arreglo 2D):** Relaciona Filas (Usuarios) con Columnas (Libros).

### Diagrama del Sistema

  +-------------------------------------------------------------------------+
  |                   SISTEMA DE GESTIÓN DE BIBLIOTECA                      |
  +-------------------------------------------------------------------------+
                                       |
                                       v
         +-----------------------------------------------------------+
         |                    MENÚ INTERACTIVO                       |
         +-----------------------------------------------------------+
               |                                           |
               v                                           v
  +--------------------------+               +--------------------------+
  |    VECTOR DE LIBROS      |               |   MATRIZ DE PRÉSTAMOS    |
  |    (Arreglo 1D)          |               |   (Arreglo 2D)           |
  +--------------------------+               +--------------------------+
  |  [0] -> El Principito    |               |         Libro 0  Libro 1 |
  |  [1] -> Cien Años...     |               |  User 0 [   1   ,   0   ] |
  |  [2] -> Rebelión Granja  |               |  User 1 [   0   ,   2   ] |
  +--------------------------+               +---------------------------+

Mapeo de la Matriz M [i] [j] 
  
  j = 0 (Libro 0)   j = 1 (Libro 1)   j = 2 (Libro 2)
        +-----------------+-----------------+-----------------+
i = 0   |        1        |        0        |        1        |  <- Usuario 0
        +-----------------+-----------------+-----------------+
i = 1   |        0        |        2        |        0        |  <- Usuario 1
        +-----------------+-----------------+-----------------+
