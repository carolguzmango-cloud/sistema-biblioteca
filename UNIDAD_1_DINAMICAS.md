\# DOCUMENTACIÓN TÉCNICA DEL SISTEMA DE BIBLIOTECA



\## 1. Estructuras de Datos



\### Vectores (listas 1D en Python)

El sistema utiliza vectores para almacenar información lineal:

\- \*\*catalogo\_libros\*\*: vector que contiene `\[ID, Título, Autor]`.

\- \*\*usuarios\*\*: vector que contiene `\[ID, Nombre]`.



\*\*Complejidad algorítmica en vectores:\*\*

\- Acceso por índice: O(1).

\- Búsqueda secuencial: O(N).

\- Inserción al final: O(1).

\- Inserción en posiciones intermedias: O(N).



\### Matrices (listas 2D en Python)

El sistema utiliza una matriz para gestionar préstamos:

\- \*\*matriz\_prestamos\*\*: cada fila contiene `\[ID\_Prestamo, ID\_Usuario, ID\_Libro, Estado]`.



\*\*Complejidad algorítmica en matrices:\*\*

\- Acceso por coordenadas (fila, columna): O(1).

\- Recorrido completo: O(N²).

\- Búsqueda por condición (ej. préstamo por ID): O(N).



\---



\## 2. Complejidad Algorítmica en el Sistema



\- \*\*mostrar\_libros()\*\*: recorre el vector → O(N).

\- \*\*registrar\_libro()\*\*: inserta al final del vector → O(1).

\- \*\*prestar\_libro()\*\*: inserta una nueva fila en la matriz → O(1).

\- \*\*devolver\_libro()\*\*: búsqueda secuencial en la matriz → O(N).

\- \*\*mostrar\_matriz\_prestamos()\*\*: recorrido completo de la matriz → O(N²).



\---



\## 3. Casos de Prueba



\### Vector de libros

\- \*\*Prueba de inserción:\*\* agregar un nuevo libro y verificar que el tamaño del vector aumente.

\- \*\*Prueba de búsqueda:\*\* recorrer el vector para confirmar que un libro existe.



\### Matriz de préstamos

\- \*\*Prueba de inserción:\*\* registrar un préstamo y verificar que la matriz tenga una nueva fila con estado `"PRESTADO"`.

\- \*\*Prueba de actualización:\*\* devolver un préstamo y confirmar que el estado cambie a `"DEVUELTO"`.

\- \*\*Prueba de error controlado:\*\* intentar devolver un préstamo inexistente y verificar que se muestre el mensaje de error.



\---



\## 4. Conclusión



El sistema implementa estructuras de datos simples (vectores y matrices) que permiten gestionar información de manera eficiente.  

\- Los vectores ofrecen acceso rápido y operaciones básicas con complejidad O(1) y O(N).  

\- Las matrices permiten representar relaciones más complejas, con recorridos de O(N²).  

\- Los casos de prueba garantizan la robustez del sistema y previenen errores en operaciones críticas como préstamos y devoluciones.



