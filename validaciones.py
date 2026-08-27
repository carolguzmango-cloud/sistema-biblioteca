# =========================
# VALIDACIONES
# =========================

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número.")


def validar_rango(numero, minimo, maximo):
    if minimo <= numero <= maximo:
        return True
    else:
        print("Error: número fuera de rango.")
        return False
