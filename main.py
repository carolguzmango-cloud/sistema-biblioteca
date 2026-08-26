# Sistema de Gestión de Biblioteca - Avance Inicial

# --- 1. USO DE VECTORES (LISTAS EN PYTHON) ---
# Vector con el catálogo inicial de libros
catalogo_libros = [
    "Estructuras de Datos en Python",
    "Cien Años de Soledad",
    "Fundamentos de Bases de Datos"
]

print("=== CATÁLOGO DE LIBROS (VECTORES) ===")
for i, libro in enumerate(catalogo_libros, 1):
    print(f"Libro {i}: {libro}")


# --- 2. USO DE MATRICES (LISTAS ANIDADAS EN PYTHON) ---
# Matriz de préstamos: [ID Estudiante, ID Libro]
matriz_prestamos = [
    [101, 1],  # Estudiante 101 pidió el Libro 1
    [102, 3]   # Estudiante 102 pidió el Libro 3
]

print("\n=== REGISTRO DE PRÉSTAMOS (MATRICES) ===")
for prestamo in matriz_prestamos:
    id_estudiante = prestamo[0]
    id_libro = prestamo[1]
    print(f"Estudiante ID: {id_estudiante} -> Prestó Libro ID: {id_libro}")
