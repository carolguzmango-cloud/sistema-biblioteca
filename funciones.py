class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        """Agregar un elemento al final de la lista."""
        nuevo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def agregar_ordenado_libro(self, nuevo_libro):
        """Inserta un libro manteniendo el orden alfabético por título."""
        nuevo = NodoDoble(nuevo_libro)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        elif nuevo_libro.titulo.lower() < self.cabeza.dato.titulo.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.dato.titulo.lower() < nuevo_libro.titulo.lower():
                actual = actual.siguiente
            
            nuevo.siguiente = actual.siguiente
            nuevo.anterior = actual
            if actual.siguiente:
                actual.siguiente.anterior = nuevo
            else:
                self.cola = nuevo
            actual.siguiente = nuevo

    def agregar_ordenado_usuario(self, nuevo_usuario):
        """Inserta un usuario manteniendo el orden alfabético por nombre."""
        nuevo = NodoDoble(nuevo_usuario)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        elif nuevo_usuario.nombre.lower() < self.cabeza.dato.nombre.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.dato.nombre.lower() < nuevo_usuario.nombre.lower():
                actual = actual.siguiente
            
            nuevo.siguiente = actual.siguiente
            nuevo.anterior = actual
            if actual.siguiente:
                actual.siguiente.anterior = nuevo
            else:
                self.cola = nuevo
            actual.siguiente = nuevo

    def buscar(self, termino, tipo="libro"):
        """Buscar elementos recorriendo la lista linealmente."""
        elementos = self.a_lista()
        termino = termino.lower()
        if tipo == "libro":
            return [l for l in elementos if termino in l.titulo.lower() or termino in l.autor.lower()]
        elif tipo == "usuario":
            return [u for u in elementos if termino in u.nombre.lower()]
        return []

    def editar(self, id_val, nuevo_titulo=None, nuevo_autor=None, nuevo_nombre=None, tipo="libro"):
        """Editar los datos de un nodo buscando por su ID único."""
        actual = self.cabeza
        while actual:
            if tipo == "libro" and actual.dato.id_libro == id_val:
                if nuevo_titulo: actual.dato.titulo = nuevo_titulo
                if nuevo_autor: actual.dato.autor = nuevo_autor
                return True
            elif tipo == "usuario" and actual.dato.id_usuario == id_val:
                if nuevo_nombre: actual.dato.nombre = nuevo_nombre
                return True
            actual = actual.siguiente
        return False

    def eliminar_por_id(self, id_val, tipo="libro"):
        """Eliminar un nodo manipulando los punteros de la lista doblemente enlazada."""
        actual = self.cabeza
        while actual:
            condicion = (actual.dato.id_libro == id_val) if tipo == "libro" else (actual.dato.id_usuario == id_val)
            if condicion:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def a_lista(self):
        """Convierte los nodos de la estructura en una lista convencional de Python."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
