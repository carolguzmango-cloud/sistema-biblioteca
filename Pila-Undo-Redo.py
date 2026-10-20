# Estructura de Datos: PILA con funciones ejecutables para Undo / Redo
class ComandoAccion:
    def __init__(self, descripcion, funcion_undo, funcion_redo):
        self.descripcion = descripcion
        self.funcion_undo = funcion_undo
        self.funcion_redo = funcion_redo

class PilaHistorialCRUD:
    def __init__(self):
        self.pila_undo = []
        self.pila_redo = []

    def registrar_y_ejecutar(self, descripcion, funcion_undo, funcion_redo):
        """Ejecuta la acción inicial, la registra en la pila de undo y limpia la pila de redo."""
        funcion_redo()
        cmd = ComandoAccion(descripcion, funcion_undo, funcion_redo)
        self.pila_undo.append(cmd)
        self.pila_redo.clear()

    def deshacer(self):
        """Saca el último comando de undo, ejecuta su función inversa y lo pasa a la pila de redo."""
        if self.pila_undo:
            cmd = self.pila_undo.pop()
            cmd.funcion_undo()
            self.pila_redo.append(cmd)
            return cmd.descripcion
        return None

    def rehacer(self):
        """Saca el último comando de redo, reejecuta la acción y lo regresa a la pila de undo."""
        if self.pila_redo:
            cmd = self.pila_redo.pop()
            cmd.funcion_redo()
            self.pila_undo.append(cmd)
            return cmd.descripcion
        return None

    def obtener_todas(self):
        """Retorna una lista con las descripciones de todas las acciones en el historial ordenadas LIFO."""
        return [cmd.descripcion for cmd in reversed(self.pila_undo)]
