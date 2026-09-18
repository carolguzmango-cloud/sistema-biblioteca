biblioteca/
├── biblioteca.py
└── funciones_adicionales.py
from funciones_adicionales import (
    eliminar_libro,
    actualizar_libro,
    ordenar_libros_por_titulo,
    registrar_usuario,
    buscar_usuario,
    eliminar_usuario,
    mostrar_usuarios,
    mostrar_matriz_usuarios_prestamos,
    mostrar_matriz_estado_libros,
    mostrar_estadisticas,
    mostrar_prestamos_usuario,
    mostrar_libros_disponibles,
    reporte_general
)


def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Eliminar libro")
    print("2. Actualizar libro")
    print("3. Ordenar libros por título")
    print("4. Eliminar usuario")
    print("5. Ver préstamos por usuario")
    print("6. Ver usuarios")
    print("7. Registrar usuario")
    print("8. Buscar usuario")
    print("9. Ver libros disponibles")
    print("10. Ver estadísticas")
    print("11. Ver reporte general")
    print("12. Mostrar matriz de usuarios y préstamos")
    print("13. Mostrar matriz de estado de libros")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            eliminar_libro()

        elif opcion == 2:
            actualizar_libro()

        elif opcion == 3:
            ordenar_libros_por_titulo()

        elif opcion == 4:
            eliminar_usuario()

        elif opcion == 5:
            mostrar_prestamos_usuario()

        elif opcion == 6:
            mostrar_usuarios()

        elif opcion == 7:
            registrar_usuario()

        elif opcion == 8:
            buscar_usuario()

        elif opcion == 9:
            mostrar_libros_disponibles()

        elif opcion == 10:
            mostrar_estadisticas()

        elif opcion == 11:
            reporte_general()

        elif opcion == 12:
            mostrar_matriz_usuarios_prestamos()

        elif opcion == 13:
            mostrar_matriz_estado_libros()

        elif opcion == 0:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

def eliminar_libro():
    print("Función para eliminar libro")


def actualizar_libro():
    print("Función para actualizar libro")


def ordenar_libros_por_titulo():
    print("Función para ordenar libros por título")


def registrar_usuario():
    print("Función para registrar usuario")


def buscar_usuario():
    print("Función para buscar usuario")


def eliminar_usuario():
    print("Función para eliminar usuario")


def mostrar_usuarios():
    print("Función para mostrar usuarios")


def mostrar_matriz_usuarios_prestamos():
    print("Matriz de usuarios y préstamos")


def mostrar_matriz_estado_libros():
    print("Matriz de estado de libros")


def mostrar_estadisticas():
    print("Estadísticas de la biblioteca")


def mostrar_prestamos_usuario():
    print("Préstamos del usuario")


def mostrar_libros_disponibles():
    print("Libros disponibles")


def reporte_general():
    print("Reporte general")

