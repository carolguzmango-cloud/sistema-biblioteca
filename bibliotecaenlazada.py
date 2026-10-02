def eliminar_por_id_libro(self, id_libro):
        """Elimina un libro de la lista doblemente enlazada ajustando los punteros."""
        actual = self.cabeza
        while actual:
            if actual.dato.id_libro == id_libro:
                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def eliminar_por_id_usuario(self, id_usuario):
        """Elimina un usuario de la lista doblemente enlazada ajustando los punteros."""
        actual = self.cabeza
        while actual:
            if actual.dato.id_usuario == id_usuario:
                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        return False
