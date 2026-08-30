import unittest
from main import buscar_libro, calcular_matriz_prestamos

class TestSistemaBiblioteca(unittest.TestCase):

    def test_buscar_libro_existente(self):
        # Caso de prueba: buscar un libro que sí existe
        self.assertTrue(buscar_libro("Cien años de soledad"))

    def test_buscar_libro_inexistente(self):
        # Caso de prueba: buscar un libro que NO existe
        self.assertFalse(buscar_libro("Libro inventado"))

    def test_calcular_matriz(self):
        # Caso de prueba: generar la matriz de préstamos
        matriz = calcular_matriz_prestamos()
        # Verificamos que sea una lista
        self.assertIsInstance(matriz, list)
        # Verificamos que tenga al menos 0 filas
        self.assertGreaterEqual(len(matriz), 0)

    def test_vector_vacio(self):
        # Caso de prueba: vector vacío
        vector = []
        # Buscar cualquier libro debe dar False
        self.assertFalse("Cien años de soledad" in vector)

    def test_matriz_vacia(self):
        # Caso de prueba: matriz vacía
        matriz = []
        # Recorrer matriz vacía no debe dar error
        for fila in matriz:
            self.assertIsInstance(fila, list)

if __name__ == "__main__":
    unittest.main()
