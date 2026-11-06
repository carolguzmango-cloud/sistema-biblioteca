import customtkinter as ctk
from tkinter import ttk, messagebox

# 1. MATRIZ (Unidad 1 - Estructuras estáticas / bidimensionales)
# Matriz 5x5 que representa la distribución física de los estantes y secciones de la biblioteca
matriz_estantes = [
    ["Sección A-1", "Sección A-2", "Sección A-3", "Sección A-4", "Sección A-5"],
    ["Sección B-1", "Sección B-2", "Sección B-3", "Sección B-4", "Sección B-5"],
    ["Sección C-1", "Sección C-2", "Sección C-3", "Sección C-4", "Sección C-5"],
    ["Sección D-1", "Sección D-2", "Sección D-3", "Sección D-4", "Sección D-5"],
    ["Sección E-1", "Sección E-2", "Sección E-3", "Sección E-4", "Sección E-5"]
]

# 2. COLA (Unidad 3 - Estructuras dinámicas FIFO)
# Estructura para gestionar la fila de usuarios en espera de libros prestados
class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaEspera:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo = NodoCola(dato)
        if not self.final:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if not self.frente:
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        return dato

    def a_lista(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

# Instancia global de la Cola de Espera
cola_espera_libros = ColaEspera()


# ==========================================
# ESTRUCTURAS DE DATOS Y POO (Unidades 1 & 2)
# ==========================================

class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.multa_acumulada = 0  # Control de multas individual

class Prestamo:
    def __init__(self, id_prestamo, usuario_nombre, libro_titulo, estado="PRESTADO"):
        self.id_prestamo = id_prestamo
        self.usuario_nombre = usuario_nombre
        self.libro_titulo = libro_titulo
        self.estado = estado

# Lista Doblemente Enlazada
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
        nuevo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def agregar_ordenado_libro(self, nuevo_libro):
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

    def eliminar_por_id(self, id_val, tipo="libro"):
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
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    # 3. RECURSIVIDAD (Unidad 3 - Algoritmos recursivos)
    # Método recursivo para contar la cantidad de elementos en la lista enlazada
    def contar_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_recursivo(nodo.siguiente)

    def ordenar_por_titulo(self):
        elementos = self.a_lista()
        n = len(elementos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if elementos[j].titulo.lower() > elementos[j + 1].titulo.lower():
                    elementos[j], elementos[j + 1] = elementos[j + 1], elementos[j]
        
        self.cabeza = None
        self.cola = None
        for elem in elementos:
            self.agregar(elem)


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
        funcion_redo()
        cmd = ComandoAccion(descripcion, funcion_undo, funcion_redo)
        self.pila_undo.append(cmd)
        self.pila_redo.clear()

    def deshacer(self):
        if self.pila_undo:
            cmd = self.pila_undo.pop()
            cmd.funcion_undo()
            self.pila_redo.append(cmd)
            return cmd.descripcion
        return None

    def rehacer(self):
        if self.pila_redo:
            cmd = self.pila_redo.pop()
            cmd.funcion_redo()
            self.pila_undo.append(cmd)
            return cmd.descripcion
        return None

    def obtener_todas(self):
        return [cmd.descripcion for cmd in reversed(self.pila_undo)]


# Instancia Global de la Pila de Historial CRUD
pila_historial = PilaHistorialCRUD()

# Carga de datos iniciales
lista_libros = ListaDoblementeEnlazada()
lista_libros.agregar_ordenado_libro(Libro("101", "Estructuras de Datos en Python", "Mark Allen Weiss"))
lista_libros.agregar_ordenado_libro(Libro("102", "Cien Años de Soledad", "Gabriel García Márquez"))
lista_libros.agregar_ordenado_libro(Libro("103", "Fundamentos de Sistemas", "Andrew Tanenbaum"))

lista_usuarios = ListaDoblementeEnlazada()
u1 = Usuario("U1", "Carol Guzmán")
u2 = Usuario("U2", "Valentina Posada")
u3 = Usuario("U3", "Camila Bustamante")
u2.multa_acumulada = 3000

lista_usuarios.agregar_ordenado_usuario(u1)
lista_usuarios.agregar_ordenado_usuario(u2)
lista_usuarios.agregar_ordenado_usuario(u3)

lista_prestamos = ListaDoblementeEnlazada()
lista_prestamos.agregar(Prestamo("P1", "Carol Guzmán", "Estructuras de Datos en Python", "PRESTADO"))
lista_prestamos.agregar(Prestamo("P2", "Valentina Posada", "Cien Años de Soledad", "DEVUELTO"))


# ==========================================
# INTERFAZ GRÁFICA (CustomTkinter)
# ==========================================

ctk.set_appearance_mode("Light")

COLOR_FONDO = "#F4F0EA"
COLOR_PANEL = "#FFFFFF"
COLOR_SIDEBAR = "#E2D4F0"
COLOR_TEXTO = "#3A3042"
COLOR_TEXTO_SUAVE = "#705D82"

COLOR_AZUL_CIELO = "#A0C4FF"
COLOR_AZUL_HOVER = "#80B3FF"
COLOR_MORADO_SUAVE = "#C8B6E2"
COLOR_TARJETA_AZUL = "#B9F3FC"
COLOR_ROJO_SUAVE = "#FFB4A2"

class AppBiblioteca(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✨ Sistema de Biblioteca - Pila Undo/Redo Integrado ✨")
        self.geometry("1150x780")
        self.configure(fg_color=COLOR_FONDO)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.configurar_estilos_tabla()
        self.crear_sidebar()

        self.panel_contenido = ctk.CTkFrame(self, fg_color="transparent")
        self.panel_contenido.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.panel_contenido.grid_columnconfigure(0, weight=1)

        self.vista_dashboard()

    def configurar_estilos_tabla(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 11, "bold"),
            background=COLOR_MORADO_SUAVE,
            foreground=COLOR_TEXTO,
            relief="flat",
            padding=8
        )
        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            background="#FFFFFF",
            foreground=COLOR_TEXTO,
            fieldbackground="#FFFFFF",
            rowheight=30,
            borderwidth=0
        )
        style.map("Treeview", background=[("selected", COLOR_AZUL_CIELO)], foreground=[("selected", "#000000")])

    def crear_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=20, fg_color=COLOR_SIDEBAR)
        sidebar.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

        lbl_logo = ctk.CTkLabel(
            sidebar, text="📚 Biblioteca 🌸", 
            font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_logo.grid(row=0, column=0, padx=20, pady=(30, 5))

        lbl_sub = ctk.CTkLabel(
            sidebar, text="Estructuras & POO", 
            font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO_SUAVE
        )
        lbl_sub.grid(row=1, column=0, padx=20, pady=(0, 25))

        opciones = [
            ("🏠 Panel Principal", self.vista_dashboard),
            ("📖 Catálogo Libros", self.vista_libros),
            ("👥 Gestión Usuarios", self.vista_usuarios),
            ("🔄 Préstamos & Multas", self.vista_prestamos),
            ("📚 Historial General", self.vista_historial)
        ]

        for idx, (texto, comando) in enumerate(opciones, start=2):
            btn = ctk.CTkButton(
                sidebar, text=texto, fg_color="transparent", 
                text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_CIELO, 
                corner_radius=12, height=40, anchor="w",
                font=ctk.CTkFont(size=14, weight="bold"),
                command=comando
            )
            btn.grid(row=idx, column=0, padx=15, pady=6, sticky="ew")

    def limpiar_panel(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

    # --- TABLAS REUTILIZABLES ---
    def mostrar_tabla_prestamos(self, row):
        frame_tabla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=12)
        frame_tabla.grid(row=row, column=0, sticky="nsew", pady=(0, 10))
        
        columnas = ("ID", "Usuario", "Libro", "Estado")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=5)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")
        
        for p in lista_prestamos.a_lista():
            tabla.insert("", "end", values=(p.id_prestamo, p.usuario_nombre, p.libro_titulo, p.estado))
        
        tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_tabla_libros(self, row):
        frame_tabla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=12)
        frame_tabla.grid(row=row, column=0, sticky="nsew", pady=(0, 10))

        columnas = ("ID", "Título", "Autor")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")

        for l in lista_libros.a_lista():
            tabla.insert("", "end", values=(l.id_libro, l.titulo, l.autor))

        tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_tabla_usuarios(self, row):
        frame_tabla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=12)
        frame_tabla.grid(row=row, column=0, sticky="nsew", pady=(0, 10))

        columnas = ("ID Usuario", "Nombre", "Multa Acumulada")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")

        for u in lista_usuarios.a_lista():
            tabla.insert("", "end", values=(u.id_usuario, u.nombre, f"${u.multa_acumulada}"))

        tabla.pack(fill="both", expand=True, padx=10, pady=10)

    # --- VISTA 1: DASHBOARD ---
    def vista_dashboard(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="¡Bienvenida al Panel de Control! ✨", 
            font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        frame_regla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_SIDEBAR, corner_radius=12)
        frame_regla.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        lbl_regla = ctk.CTkLabel(
            frame_regla, 
            text="📌 REGLA: El tiempo máximo de préstamo es de 7 días. Cada día de retraso genera una multa de $1,000.",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=COLOR_TEXTO, wraplength=750, justify="left"
        )
        lbl_regla.pack(padx=15, pady=10)

        frame_kpis = ctk.CTkFrame(self.panel_contenido, fg_color="transparent")
        frame_kpis.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        frame_kpis.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="kpi")

        prestamos_activos = sum(1 for p in lista_prestamos.a_lista() if p.estado == "PRESTADO")
        multa_total_sistema = sum(u.multa_acumulada for u in lista_usuarios.a_lista())

        self.crear_tarjeta_kpi(frame_kpis, 0, "Préstamos Activos", str(prestamos_activos), "📖", COLOR_TARJETA_AZUL)
        self.crear_tarjeta_kpi(frame_kpis, 1, "Libros", str(len(lista_libros.a_lista())), "📚", COLOR_MORADO_SUAVE)
        self.crear_tarjeta_kpi(frame_kpis, 2, "Usuarios", str(len(lista_usuarios.a_lista())), "👥", COLOR_AZUL_CIELO)
        self.crear_tarjeta_kpi(frame_kpis, 3, "Multas Pendientes", f"${multa_total_sistema}", "💸", COLOR_TARJETA_AZUL)

        lbl_sec = ctk.CTkLabel(
            self.panel_contenido, text="📋 Historial General de Préstamos", 
            font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_sec.grid(row=3, column=0, sticky="w", pady=(5, 5))

        self.mostrar_tabla_prestamos(row=4)

    def crear_tarjeta_kpi(self, parent, col, titulo, valor, icono, color_bg):
        card = ctk.CTkFrame(parent, fg_color=color_bg, corner_radius=18)
        card.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

        lbl_ico = ctk.CTkLabel(card, text=icono, font=ctk.CTkFont(size=20))
        lbl_ico.pack(anchor="w", padx=12, pady=(8, 0))

        lbl_v = ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=20, weight="bold"), text_color=COLOR_TEXTO)
        lbl_v.pack(anchor="w", padx=12, pady=(0, 0))

        lbl_t = ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=11, weight="bold"), text_color=COLOR_TEXTO_SUAVE)
        lbl_t.pack(anchor="w", padx=12, pady=(0, 8))

    # --- VISTA 2: LIBROS ---
    def vista_libros(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="📖 Catálogo de Libros (CRUD & Undo/Redo)", 
            font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        frame_undo_redo = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=14)
        frame_undo_redo.grid(row=1, column=0, sticky="ew", pady=(0, 8))

        def hacer_deshacer():
            desc = pila_historial.deshacer()
            if desc:
                messagebox.showinfo("Deshacer", f"Se deshizo: '{desc}'")
                self.vista_libros()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para deshacer.")

        def hacer_rehacer():
            desc = pila_historial.rehacer()
            if desc:
                messagebox.showinfo("Rehacer", f"Se rehizo: '{desc}'")
                self.vista_libros()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para rehacer.")

        btn_u = ctk.CTkButton(frame_undo_redo, text="↩️ Deshacer", fg_color=COLOR_MORADO_SUAVE, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, width=130, command=hacer_deshacer)
        btn_u.pack(side="left", padx=12, pady=8)

        btn_r = ctk.CTkButton(frame_undo_redo, text="🔁 Rehacer", fg_color=COLOR_AZUL_CIELO, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, width=130, command=hacer_rehacer)
        btn_r.pack(side="left", padx=5, pady=8)

        frame_form = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_form.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        e_id = ctk.CTkEntry(frame_form, placeholder_text="ID / ISBN", width=90, corner_radius=10)
        e_id.grid(row=0, column=0, padx=8, pady=12)

        e_tit = ctk.CTkEntry(frame_form, placeholder_text="Título", width=180, corner_radius=10)
        e_tit.grid(row=0, column=1, padx=8, pady=12)

        e_aut = ctk.CTkEntry(frame_form, placeholder_text="Autor", width=150, corner_radius=10)
        e_aut.grid(row=0, column=2, padx=8, pady=12)

        def agregar():
            id_val = e_id.get().strip()
            tit_val = e_tit.get().strip()
            aut_val = e_aut.get().strip()

            if not id_val or not tit_val or not aut_val:
                messagebox.showwarning("Validación", "Completa todos los campos.")
                return

            if any(l.id_libro == id_val for l in lista_libros.a_lista()):
                messagebox.showerror("Error", f"El ID '{id_val}' ya existe.")
                return

            def undo():
                lista_libros.eliminar_por_id(id_val, tipo="libro")

            def redo():
                lista_libros.agregar_ordenado_libro(Libro(id_val, tit_val, aut_val))

            pila_historial.registrar_y_ejecutar(f"Agregar Libro: {tit_val}", undo, redo)
            messagebox.showinfo("Éxito", "Libro registrado correctamente.")
            self.vista_libros()

        def editar():
            id_val = e_id.get().strip()
            tit_val = e_tit.get().strip()
            aut_val = e_aut.get().strip()

            if not id_val:
                messagebox.showwarning("Validación", "Ingresa el ID del libro a editar.")
                return

            libro_obj = next((l for l in lista_libros.a_lista() if l.id_libro == id_val), None)
            if not libro_obj:
                messagebox.showerror("Error", f"No se encontró un libro con ID '{id_val}'.")
                return

            viejo_tit = libro_obj.titulo
            viejo_aut = libro_obj.autor
            nuevo_tit = tit_val if tit_val else viejo_tit
            nuevo_aut = aut_val if aut_val else viejo_aut

            def undo():
                l = next((x for x in lista_libros.a_lista() if x.id_libro == id_val), None)
                if l:
                    l.titulo = viejo_tit
                    l.autor = viejo_aut

            def redo():
                l = next((x for x in lista_libros.a_lista() if x.id_libro == id_val), None)
                if l:
                    l.titulo = nuevo_tit
                    l.autor = nuevo_aut

            pila_historial.registrar_y_ejecutar(f"Editar Libro ID: {id_val}", undo, redo)
            messagebox.showinfo("Éxito", f"Libro '{id_val}' actualizado.")
            self.vista_libros()

        def eliminar():
            id_val = e_id.get().strip()
            if not id_val:
                messagebox.showwarning("Validación", "Ingresa el ID del libro a eliminar.")
                return

            libro_a_borrar = next((l for l in lista_libros.a_lista() if l.id_libro == id_val), None)
            if not libro_a_borrar:
                messagebox.showerror("Error", f"No se encontró el libro con ID '{id_val}'.")
                return

            b_id = libro_a_borrar.id_libro
            b_tit = libro_a_borrar.titulo
            b_aut = libro_a_borrar.autor

            def undo():
                lista_libros.agregar_ordenado_libro(Libro(b_id, b_tit, b_aut))

            def redo():
                lista_libros.eliminar_por_id(b_id, tipo="libro")

            pila_historial.registrar_y_ejecutar(f"Eliminar Libro: {b_tit}", undo, redo)
            messagebox.showinfo("Éxito", f"Libro ID '{id_val}' eliminado.")
            self.vista_libros()

        btn_add = ctk.CTkButton(frame_form, text="➕ Agregar", fg_color=COLOR_AZUL_CIELO, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, width=80, command=agregar)
        btn_add.grid(row=0, column=3, padx=4, pady=12)

        btn_edit = ctk.CTkButton(frame_form, text="✏️ Editar", fg_color=COLOR_MORADO_SUAVE, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, width=80, command=editar)
        btn_edit.grid(row=0, column=4, padx=4, pady=12)

        btn_del = ctk.CTkButton(frame_form, text="🗑️ Eliminar", fg_color=COLOR_ROJO_SUAVE, hover_color="#FF9B85", text_color=COLOR_TEXTO, width=80, command=eliminar)
        btn_del.grid(row=0, column=5, padx=4, pady=12)

        self.mostrar_tabla_libros(row=3)

    # --- VISTA 3: USUARIOS ---
    def vista_usuarios(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="👥 Gestión de Usuarios (CRUD & Undo/Redo)", 
            font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        frame_undo_redo = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=14)
        frame_undo_redo.grid(row=1, column=0, sticky="ew", pady=(0, 8))

        def hacer_deshacer_u():
            desc = pila_historial.deshacer()
            if desc:
                messagebox.showinfo("Deshacer", f"Se deshizo: '{desc}'")
                self.vista_usuarios()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para deshacer.")

        def hacer_rehacer_u():
            desc = pila_historial.rehacer()
            if desc:
                messagebox.showinfo("Rehacer", f"Se rehizo: '{desc}'")
                self.vista_usuarios()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para rehacer.")

        btn_u = ctk.CTkButton(frame_undo_redo, text="↩️ Deshacer", fg_color=COLOR_MORADO_SUAVE, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, width=130, command=hacer_deshacer_u)
        btn_u.pack(side="left", padx=12, pady=8)

        btn_r = ctk.CTkButton(frame_undo_redo, text="🔁 Rehacer", fg_color=COLOR_AZUL_CIELO, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, width=130, command=hacer_rehacer_u)
        btn_r.pack(side="left", padx=5, pady=8)

        frame_form = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_form.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        e_id_user = ctk.CTkEntry(frame_form, placeholder_text="ID (ej: U4)", width=100, corner_radius=10)
        e_id_user.grid(row=0, column=0, padx=10, pady=12)

        e_nombre = ctk.CTkEntry(frame_form, placeholder_text="Nombre Completo", width=220, corner_radius=10)
        e_nombre.grid(row=0, column=1, padx=10, pady=12)

        def agregar_usuario():
            id_u = e_id_user.get().strip()
            nombre_u = e_nombre.get().strip()

            if not id_u or not nombre_u:
                messagebox.showwarning("Validación", "Ingresa ID y Nombre.")
                return

            if any(u.id_usuario == id_u for u in lista_usuarios.a_lista()):
                messagebox.showerror("Error", f"El ID '{id_u}' ya existe.")
                return

            def undo():
                lista_usuarios.eliminar_por_id(id_u, tipo="usuario")

            def redo():
                lista_usuarios.agregar_ordenado_usuario(Usuario(id_u, nombre_u))

            pila_historial.registrar_y_ejecutar(f"Agregar Usuario: {nombre_u}", undo, redo)
            messagebox.showinfo("Éxito", f"Usuario '{nombre_u}' registrado.")
            self.vista_usuarios()

        def editar_usuario():
            id_u = e_id_user.get().strip()
            nombre_u = e_nombre.get().strip()

            if not id_u:
                messagebox.showwarning("Validación", "Ingresa el ID del usuario a editar.")
                return

            usr = next((u for u in lista_usuarios.a_lista() if u.id_usuario == id_u), None)
            if not usr:
                messagebox.showerror("Error", f"No se encontró el usuario ID '{id_u}'.")
                return

            viejo_nombre = usr.nombre
            nuevo_nombre = nombre_u if nombre_u else viejo_nombre

            def undo():
                u = next((x for x in lista_usuarios.a_lista() if x.id_usuario == id_u), None)
                if u: u.nombre = viejo_nombre

            def redo():
                u = next((x for x in lista_usuarios.a_lista() if x.id_usuario == id_u), None)
                if u: u.nombre = nuevo_nombre

            pila_historial.registrar_y_ejecutar(f"Editar Usuario ID: {id_u}", undo, redo)
            messagebox.showinfo("Éxito", f"Usuario ID '{id_u}' actualizado.")
            self.vista_usuarios()

        def eliminar_usuario():
            id_u = e_id_user.get().strip()
            if not id_u:
                messagebox.showwarning("Validación", "Ingresa el ID del usuario a eliminar.")
                return

            usr_a_borrar = next((u for u in lista_usuarios.a_lista() if u.id_usuario == id_u), None)
            if not usr_a_borrar:
                messagebox.showerror("Error", f"No se encontró el usuario ID '{id_u}'.")
                return

            u_id = usr_a_borrar.id_usuario
            u_nombre = usr_a_borrar.nombre

            def undo():
                lista_usuarios.agregar_ordenado_usuario(Usuario(u_id, u_nombre))

            def redo():
                lista_usuarios.eliminar_por_id(u_id, tipo="usuario")

            pila_historial.registrar_y_ejecutar(f"Eliminar Usuario: {u_nombre}", undo, redo)
            messagebox.showinfo("Éxito", f"Usuario ID '{id_u}' eliminado.")
            self.vista_usuarios()

        btn_add_u = ctk.CTkButton(frame_form, text="➕ Agregar", fg_color=COLOR_AZUL_CIELO, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, width=95, command=agregar_usuario)
        btn_add_u.grid(row=0, column=2, padx=5, pady=12)

        btn_edit_u = ctk.CTkButton(frame_form, text="✏️ Editar", fg_color=COLOR_MORADO_SUAVE, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, width=95, command=editar_usuario)
        btn_edit_u.grid(row=0, column=3, padx=5, pady=12)

        btn_del_u = ctk.CTkButton(frame_form, text="🗑️ Eliminar", fg_color=COLOR_ROJO_SUAVE, hover_color="#FF9B85", text_color=COLOR_TEXTO, width=95, command=eliminar_usuario)
        btn_del_u.grid(row=0, column=4, padx=5, pady=12)

        self.mostrar_tabla_usuarios(row=3)

    # --- VISTA 4: PRÉSTAMOS & MULTAS ---
    def vista_prestamos(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="🔄 Préstamos & Multas", 
            font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        nombres_usuarios = [u.nombre for u in lista_usuarios.a_lista()] or ["Sin usuarios"]

        frame_nuevo_p = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_nuevo_p.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        cb_usuario = ctk.CTkComboBox(frame_nuevo_p, values=nombres_usuarios, width=180, corner_radius=10)
        cb_usuario.grid(row=0, column=0, padx=10, pady=10)

        e_titulo_libro = ctk.CTkEntry(frame_nuevo_p, placeholder_text="Título exacto del Libro", width=220, corner_radius=10)
        e_titulo_libro.grid(row=0, column=1, padx=10, pady=10)

        def registrar_prestamo():
            usuario_sel = cb_usuario.get().strip()
            titulo_sel = e_titulo_libro.get().strip()

            if not usuario_sel or not titulo_sel:
                messagebox.showwarning("Validación", "Selecciona un usuario e ingresa el título del libro.")
                return

            libro_existente = next((l for l in lista_libros.a_lista() if l.titulo.lower() == titulo_sel.lower()), None)
            if not libro_existente:
                messagebox.showerror("Error", f"El libro '{titulo_sel}' no existe.")
                return

            nuevo_id_p = f"P{len(lista_prestamos.a_lista()) + 1}"
            
            def undo():
                actual = lista_prestamos.cabeza
                while actual:
                    if actual.dato.id_prestamo == nuevo_id_p:
                        if actual.anterior: actual.anterior.siguiente = actual.siguiente
                        else: lista_prestamos.cabeza = actual.siguiente
                        if actual.siguiente: actual.siguiente.anterior = actual.anterior
                        else: lista_prestamos.cola = actual.anterior
                        break
                    actual = actual.siguiente

            def redo():
                lista_prestamos.agregar(Prestamo(nuevo_id_p, usuario_sel, libro_existente.titulo, "PRESTADO"))

            pila_historial.registrar_y_ejecutar(f"Préstamo {nuevo_id_p} a {usuario_sel}", undo, redo)
            messagebox.showinfo("Éxito", f"Préstamo '{nuevo_id_p}' asignado a {usuario_sel}.")
            self.vista_prestamos()

        btn_p = ctk.CTkButton(frame_nuevo_p, text="📖 Solicitar Préstamo", fg_color=COLOR_AZUL_CIELO, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, command=registrar_prestamo)
        btn_p.grid(row=0, column=2, padx=10, pady=10)

        frame_dev = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_dev.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        e_id_p = ctk.CTkEntry(frame_dev, placeholder_text="ID Préstamo (ej: P1)", width=140, corner_radius=10)
        e_id_p.grid(row=0, column=0, padx=10, pady=10)

        e_dias = ctk.CTkEntry(frame_dev, placeholder_text="Días transcurridos", width=140, corner_radius=10)
        e_dias.grid(row=0, column=1, padx=10, pady=10)

        def devolver():
            id_p = e_id_p.get().strip()
            dias_str = e_dias.get().strip()

            if not id_p or not dias_str.isdigit():
                messagebox.showwarning("Validación", "Ingresa un ID válido y número de días entero.")
                return

            dias = int(dias_str)
            prestamo_obj = next((p for p in lista_prestamos.a_lista() if p.id_prestamo == id_p), None)
            if not prestamo_obj:
                messagebox.showerror("Error", f"Préstamo '{id_p}' no encontrado.")
                return

            estado_viejo = prestamo_obj.estado
            prestamo_obj.estado = "DEVUELTO"
            multa_generada = (dias - 7) * 1000 if dias > 7 else 0

            usr_obj = next((u for u in lista_usuarios.a_lista() if u.nombre == prestamo_obj.usuario_nombre), None)
            multa_anterior = usr_obj.multa_acumulada if usr_obj else 0
            if usr_obj and multa_generada > 0:
                usr_obj.multa_acumulada += multa_generada
                messagebox.showwarning("Multa Generada", f"Devolución con retraso.\nMulta de ${multa_generada} cargada a {usr_obj.nombre}.")
            else:
                messagebox.showinfo("Éxito", "Libro devuelto a tiempo.")

            def undo():
                p_obj = next((p for p in lista_prestamos.a_lista() if p.id_prestamo == id_p), None)
                if p_obj: p_obj.estado = estado_viejo
                if usr_obj: usr_obj.multa_acumulada = multa_anterior

            def redo():
                p_obj = next((p for p in lista_prestamos.a_lista() if p.id_prestamo == id_p), None)
                if p_obj: p_obj.estado = "DEVUELTO"
                if usr_obj and multa_generada > 0: usr_obj.multa_acumulada += multa_generada

            pila_historial.registrar_y_ejecutar(f"Devolución de {id_p}", undo, redo)
            self.vista_prestamos()

        btn_dev = ctk.CTkButton(frame_dev, text="🔄 Devolver Libro", fg_color=COLOR_MORADO_SUAVE, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, command=devolver)
        btn_dev.grid(row=0, column=2, padx=10, pady=10)

        lbl_tabla_p = ctk.CTkLabel(self.panel_contenido, text="📋 Registro de Préstamos", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXTO)
        lbl_tabla_p.grid(row=3, column=0, sticky="w", pady=(5, 5))
        self.mostrar_tabla_prestamos(row=4)

        lbl_deudas = ctk.CTkLabel(self.panel_contenido, text="💰 Control de Multas por Usuario", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXTO)
        lbl_deudas.grid(row=5, column=0, sticky="w", pady=(10, 5))

        frame_pago = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_pago.grid(row=6, column=0, sticky="ew", pady=(0, 10))

        cb_usuario_pago = ctk.CTkComboBox(frame_pago, values=nombres_usuarios, width=200, corner_radius=10)
        cb_usuario_pago.grid(row=0, column=0, padx=15, pady=10)

        def pagar_multa():
            usr_nombre = cb_usuario_pago.get().strip()
            usr = next((u for u in lista_usuarios.a_lista() if u.nombre == usr_nombre), None)
            if not usr or usr.multa_acumulada == 0:
                messagebox.showinfo("Aviso", "El usuario no tiene multas pendientes.")
                return

            m_anterior = usr.multa_acumulada
            usr.multa_acumulada = 0

            def undo():
                u_obj = next((x for x in lista_usuarios.a_lista() if x.nombre == usr_nombre), None)
                if u_obj: u_obj.multa_acumulada = m_anterior

            def redo():
                u_obj = next((x for x in lista_usuarios.a_lista() if x.nombre == usr_nombre), None)
                if u_obj: u_obj.multa_acumulada = 0

            pila_historial.registrar_y_ejecutar(f"Pago de Multa de {usr_nombre}", undo, redo)
            messagebox.showinfo("Éxito", f"Multa de {usr_nombre} pagada por completo.")
            self.vista_prestamos()

        btn_pagar = ctk.CTkButton(frame_pago, text="💳 Pagar Multa", fg_color=COLOR_AZUL_CIELO, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, command=pagar_multa)
        btn_pagar.grid(row=0, column=1, padx=15, pady=10)

    # --- VISTA 5: HISTORIAL GENERAL DE OPERACIONES (PILA UNDO/REDO) ---
    def vista_historial(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="📚 Historial General de Operaciones (Pila)", 
            font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        frame_acciones = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=14)
        frame_acciones.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        def ejecutar_deshacer():
            desc = pila_historial.deshacer()
            if desc:
                messagebox.showinfo("Deshacer", f"Se deshizo: '{desc}'")
                self.vista_historial()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para deshacer.")

        def ejecutar_rehacer():
            desc = pila_historial.rehacer()
            if desc:
                messagebox.showinfo("Rehacer", f"Se rehizo: '{desc}'")
                self.vista_historial()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para rehacer.")

        btn_u = ctk.CTkButton(frame_acciones, text="↩️ Deshacer Última Acción", fg_color=COLOR_MORADO_SUAVE, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, command=ejecutar_deshacer)
        btn_u.pack(side="left", padx=15, pady=10)

        btn_r = ctk.CTkButton(frame_acciones, text="🔁 Rehacer Acción", fg_color=COLOR_AZUL_CIELO, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, command=ejecutar_rehacer)
        btn_r.pack(side="left", padx=10, pady=10)

        frame_lista = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_lista.grid(row=2, column=0, sticky="nsew", pady=(0, 10))

        lbl_top = ctk.CTkLabel(frame_lista, text="Pila de Historial (Más reciente arriba):", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXTO)
        lbl_top.pack(anchor="w", padx=15, pady=(10, 5))

        historial = pila_historial.obtener_todas()
        if not historial:
            lbl_vacio = ctk.CTkLabel(frame_lista, text="No hay operaciones registradas en la pila aún.", text_color=COLOR_TEXTO_SUAVE)
            lbl_vacio.pack(padx=15, pady=15)
        else:
            for i, desc in enumerate(historial, start=1):
                lbl_item = ctk.CTkLabel(frame_lista, text=f"{i}. {desc}", font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO, anchor="w")
                lbl_item.pack(fill="x", padx=20, pady=3)


# ==========================================
# INICIALIZACIÓN DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    app = AppBiblioteca()
    app.mainloop()