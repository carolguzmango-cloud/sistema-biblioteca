# Sistema de Gestión de Biblioteca - Avance Inicial
catalogo_libros = [
    "Estructuras de Datos en Python",
    "Cien Años de Soledad",
    "Fundamentos de Bases de Datos"
]

print("=== CATÁLOGO DE LIBROS (VECTORES) ===")
for i, libro in enumerate(catalogo_libros, 1):
    print(f"Libro {i}: {libro}")


#USO DE MATRICES 
matriz_prestamos = [
    [101, 1],  
    [102, 3]   
]

print("\n=== REGISTRO DE PRÉSTAMOS (MATRICES) ===")
for prestamo in matriz_prestamos:
    id_estudiante = prestamo[0]
    id_libro = prestamo[1]
    print(f"Estudiante ID: {id_estudiante} -> Prestó Libro ID: {id_libro}")
