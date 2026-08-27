# ===== sistema de devoluciones, multas y busqueda de  libros por autor  =====

multas = []


# Busqueda de libros por autor
def buscar_por_autor():
    autor = input("Autor que desea buscar: ")

    for libro in catalogo_libros:
        if libro[2].lower() == autor.lower():
            print("ID:", libro[0], "| Libro:", libro[1])

    print("Búsqueda terminada.")


# Devolver libro y calcular multa
def devolver_con_multa():
    id_prestamo = input("ID del préstamo: ")

    for prestamo in matriz_prestamos:
        if prestamo[0] == id_prestamo:

            dias = int(input("Días que tuvo el libro: "))

            prestamo[3] = "DEVUELTO"

            if dias > 7:
                multa = (dias - 7) * 1000
            else:
                multa = 0

            multas.append(multa)

            print("Libro devuelto.")
            print("Multa: $", multa)
            return

    print("Préstamo no encontrado.")


# Mostrar multas
def mostrar_multas():
    print("\n--- MULTAS ---")

    for multa in multas:
        print("$", multa)
