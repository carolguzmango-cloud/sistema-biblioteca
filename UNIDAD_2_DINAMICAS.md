# Documentación Técnica - Unidad 2: Estructuras de Datos Dinámicas

## Objetivo de la Unidad
Implementar y aplicar estructuras de datos dinámicas (específicamente *Listas Doblemente Enlazadas*) en Python para la gestión eficiente de elementos en el Sistema de Gestión de Biblioteca, optimizando el uso de memoria en comparación con las estructuras estáticas.

---

## Componentes Implementados en el Código (unidad_2.py)

### 1. Clase NodoDoble
Representa cada elemento individual dentro de la memoria dinámica. Contiene los datos del objeto y dos punteros para la navegación bidireccional:
* self.dato: Almacena la información (Libro, Usuario o Préstamo).
* self.siguiente: Referencia al nodo posterior.
* self.anterior: Referencia al nodo anterior.

### 2. Clase ListaDoblementeEnlazada
Administra la conexión y el flujo de los nodos en tiempo de ejecución:
* *Método agregar(dato):* Inserta un nuevo nodo al final de la estructura de manera dinámica ajustando los punteros cabeza y cola.
* *Método a_lista():* Recorre la estructura enlazada convirtiéndola temporalmente en un arreglo convencional para facilitar su renderizado en las tablas gráficas de la interfaz (ttk.Treeview).

---

## Aplicación Práctica en el Sistema
En este proyecto, las listas doblemente enlazadas se utilizan para gestionar de forma dinámica:
* El *catálogo de libros* disponibles.
* La *lista de usuarios* registrados y sus multas.
* El *historial de préstamos* activos y devueltos.
