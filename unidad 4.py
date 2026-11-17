import customtkinter as ctk
from tkinter import ttk, messagebox

# ==========================================
# 1. MATRIZ (Estructura Estática / Bidimensional)
# ==========================================
matriz_estantes = [
    ["Sección A-1", "Sección A-2", "Sección A-3", "Sección A-4", "Sección A-5"],
    ["Sección B-1", "Sección B-2", "Sección B-3", "Sección B-4", "Sección B-5"],
    ["Sección C-1", "Sección C-2", "Sección C-3", "Sección C-4", "Sección C-5"],
    ["Sección D-1", "Sección D-2", "Sección D-3", "Sección D-4", "Sección D-5"],
    ["Sección E-1", "Sección E-2", "Sección E-3", "Sección E-4", "Sección E-5"]
]

# ==========================================
# 2. COLA (Estructura Dinámica FIFO - Espera)
# ==========================================
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

cola_espera_libros = ColaEspera()

# ==========================================
# 3. PILA DINÁMICA CON NODOS (LIFO - Undo/Redo)
# ==========================================
class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaDinamica:
    def __init__(self):
        self.cima = None

    def esta_vacia(self):
        return self.cima is None

    def apilar(self, dato):
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def desapilar(self):
        if self.esta_vacia():
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def limpiar(self):
        self.cima = None

    def obtener_elementos(self):
        elementos = []
        actual = self.cima
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

class ComandoAccion:
    def __init__(self, descripcion, funcion_undo, funcion_redo):
        self.descripcion = descripcion
        self.funcion_undo = funcion_undo
        self.funcion_redo = funcion_redo

class PilaHistorialCRUD:
    def __init__(self):
        self.pila_undo = PilaDinamica()
        self.pila_redo = PilaDinamica()

    def registrar_y_ejecutar(self, descripcion, funcion_undo, funcion_redo):
        funcion_redo()
        cmd = ComandoAccion(descripcion, funcion_undo, funcion_redo)
        self.pila_undo.apilar(cmd)
        self.pila_redo.limpiar()

    def deshacer(self):
        if not self.pila_undo.esta_vacia():
            cmd = self.pila_undo.desapilar()
            cmd.funcion_undo()
            self.pila_redo.apilar(cmd)
            return cmd.descripcion
        return None

    def rehacer(self):
        if not self.pila_redo.esta_vacia():
            cmd = self.pila_redo.desapilar()
            cmd.funcion_redo()
            self.pila_undo.apilar(cmd)
            return cmd.descripcion
        return None

    def obtener_todas(self):
        return [cmd.descripcion for cmd in self.pila_undo.obtener_elementos()]

pila_historial = PilaHistorialCRUD()

# ==========================================
# 4. ÁRBOL BINARIO DE BÚSQUEDA (BST)
# ==========================================
class NodoArbol:
    def __init__(self, libro):
        self.libro = libro
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, libro):
        if not self.raiz:
            self.raiz = NodoArbol(libro)
        else:
            self._insertar_recursivo(self.raiz, libro)

    def _insertar_recursivo(self, actual, libro):
        if libro.titulo.lower() < actual.libro.titulo.lower():
            if not actual.izquierdo:
                actual.izquierdo = NodoArbol(libro)
            else:
                self._insertar_recursivo(actual.izquierdo, libro)
        else:
            if not actual.derecho:
                actual.derecho = NodoArbol(libro)
            else:
                self._insertar_recursivo(actual.derecho, libro)

    def recorrido_inorden(self):
        elementos = []
        self._inorden_recursivo(self.raiz, elementos)
        return elementos

    def _inorden_recursivo(self, actual, elementos):
        if actual:
            self._inorden_recursivo(actual.izquierdo, elementos)
            elementos.append(actual.libro)
            self._inorden_recursivo(actual.derecho, elementos)

    def buscar(self, titulo):
        return self._buscar_recursivo(self.raiz, titulo.lower().strip())

    def _buscar_recursivo(self, actual, titulo_buscado):
        if not actual:
            return None
        if actual.libro.titulo.lower() == titulo_buscado:
            return actual.libro
        if titulo_buscado < actual.libro.titulo.lower():
            return self._buscar_recursivo(actual.izquierdo, titulo_buscado)
        return self._buscar_recursivo(actual.derecho, titulo_buscado)

arbol_libros = ArbolBinarioBusqueda()

# ==========================================
# 5. MODELOS (Clases POO y Listas Doblemente Enlazadas)
# ==========================================
class Libro:
    def __init__(self, id_libro, titulo, autor, genero):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.multa_acumulada = 0

class Prestamo:
    def __init__(self, id_prestamo, usuario_nombre, libro_titulo, estado="PRESTADO"):
        self.id_prestamo = id_prestamo
        self.usuario_nombre = usuario_nombre
        self.libro_titulo = libro_titulo
        self.estado = estado

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
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

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

# Carga de los 15 libros iniciales con su respectivo género
lista_libros = ListaDoblementeEnlazada()
libros_iniciales = [
    Libro("101", "Estructuras de Datos en Python", "Mark Allen Weiss", "Programación"),
    Libro("102", "Cien Años de Soledad", "Gabriel García Márquez", "Literatura"),
    Libro("103", "Fundamentos de Sistemas", "Andrew Tanenbaum", "Ingeniería"),
    Libro("104", "Clean Code", "Robert C. Martin", "Programación"),
    Libro("105", "El Hobbit", "J.R.R. Tolkien", "Fantasía"),
    Libro("106", "Don Quijote de la Mancha", "Miguel de Cervantes", "Literatura"),
    Libro("107", "Algoritmos en C++", "Sedgewick", "Programación"),
    Libro("108", "Rebelión en la Granja", "George Orwell", "Literatura"),
    Libro("109", "Crimen y Castigo", "Fiódor Dostoyevski", "Literatura"),
    Libro("110", "Inteligencia Artificial: Un Enfoque Moderno", "Stuart Russell", "Ingeniería"),
    Libro("111", "Redes de Computadoras", "James F. Kurose", "Ingeniería"),
    Libro("112", "Principios de Administración Financiera", "Gitman", "Finanzas"),
    Libro("113", "La Metamorfosis", "Franz Kafka", "Literatura"),
    Libro("114", "Matemáticas Discretas", "Kenneth Rosen", "Ciencias Exactas"),
    Libro("115", "Cálculo de Una Variable", "James Stewart", "Ciencias Exactas")
]

for l in libros_iniciales:
    lista_libros.agregar(l)
    arbol_libros.insertar(l)

# 5 usuarios iniciales
lista_usuarios = ListaDoblementeEnlazada()
u1 = Usuario("U1", "Carol Guzmán")
u2 = Usuario("U2", "Valentina Posada")
u3 = Usuario("U3", "Camila Bustamante")
u4 = Usuario("U4", "Andrés Gómez")
u5 = Usuario("U5", "Lucía Pérez")
u2.multa_acumulada = 3000
for u in [u1, u2, u3, u4, u5]:
    lista_usuarios.agregar(u)

lista_prestamos = ListaDoblementeEnlazada()
lista_prestamos.agregar(Prestamo("P1", "Carol Guzmán", "Estructuras de Datos en Python", "PRESTADO"))
lista_prestamos.agregar(Prestamo("P2", "Valentina Posada", "Cien Años de Soledad", "DEVUELTO"))

# ==========================================
# 6. INTERFAZ GRÁFICA (CustomTkinter)
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

class AppBiblioteca(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("✨ Sistema Inteligente de Biblioteca - Árbol BST & Géneros ✨")
        self.geometry("1180x850")
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
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background=COLOR_MORADO_SUAVE, foreground=COLOR_TEXTO, relief="flat", padding=8)
        style.configure("Treeview", font=("Segoe UI", 10), background="#FFFFFF", foreground=COLOR_TEXTO, fieldbackground="#FFFFFF", rowheight=28, borderwidth=0)
        style.map("Treeview", background=[("selected", COLOR_AZUL_CIELO)], foreground=[("selected", "#000000")])

    def crear_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=20, fg_color=COLOR_SIDEBAR)
        sidebar.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

        lbl_logo = ctk.CTkLabel(sidebar, text="📚 Biblioteca 🌸", font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO)
        lbl_logo.grid(row=0, column=0, padx=20, pady=(30, 5))

        lbl_sub = ctk.CTkLabel(sidebar, text="Proyecto U. Amigó", font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO_SUAVE)
        lbl_sub.grid(row=1, column=0, padx=20, pady=(0, 25))

        opciones = [
            ("🏠 Panel Principal", self.vista_dashboard),
            ("🌳 Catálogo & Árbol BST", self.vista_libros),
            ("👥 Gestión Usuarios", self.vista_usuarios),
            ("🔄 Préstamos & Multas", self.vista_prestamos),
            ("📜 Historial (Pila)", self.vista_historial),
        ]

        for idx, (texto, comando) in enumerate(opciones, start=2):
            btn = ctk.CTkButton(sidebar, text=texto, fg_color="transparent", text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_CIELO, corner_radius=12, height=40, anchor="w", font=ctk.CTkFont(size=14, weight="bold"), command=comando)
            btn.grid(row=idx, column=0, padx=15, pady=6, sticky="ew")

    def limpiar_panel(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

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
        # Agregamos la columna de Género en la tabla
        columnas = ("ID", "Título (Ordenado por Árbol BST)", "Autor", "Género")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=14)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")
        for l in arbol_libros.recorrido_inorden():
            tabla.insert("", "end", values=(l.id_libro, l.titulo, l.autor, l.genero))
        tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_tabla_usuarios(self, row):
        frame_tabla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=12)
        frame_tabla.grid(row=row, column=0, sticky="nsew", pady=(0, 10))
        columnas = ("ID Usuario", "Nombre", "Multa Acumulada")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=6)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")
        for u in lista_usuarios.a_lista():
            tabla.insert("", "end", values=(u.id_usuario, u.nombre, f"${u.multa_acumulada}"))
        tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def vista_dashboard(self):
        self.limpiar_panel()
        lbl_titulo = ctk.CTkLabel(self.panel_contenido, text="✨ ¡Bienvenida al Panel de Control! ✨", font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXTO)
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        frame_regla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_SIDEBAR, corner_radius=12)
        frame_regla.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        lbl_regla = ctk.CTkLabel(frame_regla, text="📌 REGLA: El tiempo máximo de préstamo es de 7 días. Cada día de retraso genera una multa de $1,000.", font=ctk.CTkFont(size=12, weight="bold"), text_color=COLOR_TEXTO, wraplength=750, justify="left")
        lbl_regla.pack(padx=15, pady=10)

        frame_kpis = ctk.CTkFrame(self.panel_contenido, fg_color="transparent")
        frame_kpis.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        frame_kpis.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="kpi")

        prestamos_activos = sum(1 for p in lista_prestamos.a_lista() if p.estado == "PRESTADO")
        multa_total = sum(u.multa_acumulada for u in lista_usuarios.a_lista())

        self.crear_tarjeta_kpi(frame_kpis, 0, "Préstamos Activos", str(prestamos_activos), "📖", COLOR_TARJETA_AZUL)
        self.crear_tarjeta_kpi(frame_kpis, 1, "Libros en Árbol", str(len(arbol_libros.recorrido_inorden())), "🌳", COLOR_MORADO_SUAVE)
        self.crear_tarjeta_kpi(frame_kpis, 2, "Usuarios", str(len(lista_usuarios.a_lista())), "👥", COLOR_AZUL_CIELO)
        self.crear_tarjeta_kpi(frame_kpis, 3, "Multas Pendientes", f"${multa_total}", "💰", COLOR_TARJETA_AZUL)

        lbl_sec = ctk.CTkLabel(self.panel_contenido, text="📋 Historial General de Préstamos", font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXTO)
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

    def vista_libros(self):
        self.limpiar_panel()
        lbl_titulo = ctk.CTkLabel(self.panel_contenido, text="🌳 Catálogo de Libros, Árbol BST & Géneros", font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO)
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Panel de Búsqueda Inteligente (Título o Género)
        frame_busqueda = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_SIDEBAR, corner_radius=14)
        frame_busqueda.grid(row=1, column=0, sticky="ew", pady=(0, 8))

        e_buscar = ctk.CTkEntry(frame_busqueda, placeholder_text="Escribe título o género (ej: Programación)...", width=310, corner_radius=10)
        e_buscar.pack(side="left", padx=12, pady=10)

        def buscar_inteligente():
            termino = e_buscar.get().strip()
            if not termino:
                messagebox.showwarning("Validación", "Ingresa un título o género para buscar.")
                return
            
            # 1. Intentar buscar primero por título exacto en el Árbol BST
            resultado_bst = arbol_libros.buscar(termino)
            if resultado_bst:
                messagebox.showinfo("¡Libro Encontrado (BST)! 🌳", f"✅ Encontrado en el Árbol:\n\nID: {resultado_bst.id_libro}\nTítulo: {resultado_bst.titulo}\nAutor: {resultado_bst.autor}\nGénero: {resultado_bst.genero}")
                return

            # 2. Si no es un título exacto, buscar por género en toda la lista
            coincidencias = [l for l in arbol_libros.recorrido_inorden() if termino.lower() in l.genero.lower()]
            if coincidencias:
                nombres = "\n".join([f"• {l.titulo} ({l.autor})" for l in coincidencias])
                messagebox.showinfo(f"📚 Libros de '{termino}'", f"Se encontraron {len(coincidencias)} libros en este género:\n\n{nombres}")
            else:
                messagebox.showerror("No encontrado", f"❌ No se encontró ningún libro o género con el término '{termino}'.")

        btn_buscar = ctk.CTkButton(frame_busqueda, text="🔍 Buscar por Título/Género", fg_color=COLOR_AZUL_CIELO, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, command=buscar_inteligente)
        btn_buscar.pack(side="left", padx=5, pady=10)

        frame_undo_redo = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=14)
        frame_undo_redo.grid(row=2, column=0, sticky="ew", pady=(0, 8))

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

        # Formulario para Agregar Nuevos Libros con Género
        frame_form = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_form.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        e_id = ctk.CTkEntry(frame_form, placeholder_text="ID", width=70, corner_radius=10)
        e_id.grid(row=0, column=0, padx=6, pady=12)
        e_tit = ctk.CTkEntry(frame_form, placeholder_text="Título", width=160, corner_radius=10)
        e_tit.grid(row=0, column=1, padx=6, pady=12)
        e_aut = ctk.CTkEntry(frame_form, placeholder_text="Autor", width=130, corner_radius=10)
        e_aut.grid(row=0, column=2, padx=6, pady=12)
        e_gen = ctk.CTkEntry(frame_form, placeholder_text="Género", width=120, corner_radius=10)
        e_gen.grid(row=0, column=3, padx=6, pady=12)

        def agregar():
            id_val = e_id.get().strip()
            tit_val = e_tit.get().strip()
            aut_val = e_aut.get().strip()
            gen_val = e_gen.get().strip()

            if not id_val or not tit_val or not aut_val or not gen_val:
                messagebox.showwarning("Validación", "Completa todos los campos (incluyendo el género).")
                return

            if any(l.id_libro == id_val for l in lista_libros.a_lista()):
                messagebox.showerror("Error", f"El ID '{id_val}' ya existe.")
                return

            nuevo_libro = Libro(id_val, tit_val, aut_val, gen_val)

            def undo():
                lista_libros.eliminar_por_id(id_val, tipo="libro")
                global arbol_libros
                arbol_libros = ArbolBinarioBusqueda()
                for l in lista_libros.a_lista():
                    arbol_libros.insertar(l)

            def redo():
                lista_libros.agregar(nuevo_libro)
                arbol_libros.insertar(nuevo_libro)

            pila_historial.registrar_y_ejecutar(f"Agregar Libro: {tit_val}", undo, redo)
            messagebox.showinfo("Éxito", "Libro registrado con género e indexado en el Árbol BST.")
            self.vista_libros()

        btn_add = ctk.CTkButton(frame_form, text="➕ Agregar", fg_color=COLOR_AZUL_CIELO, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, width=80, command=agregar)
        btn_add.grid(row=0, column=4, padx=6, pady=12)

        self.mostrar_tabla_libros(row=4)

    def vista_usuarios(self):
        self.limpiar_panel()
        lbl_titulo = ctk.CTkLabel(self.panel_contenido, text="👥 Gestión de Usuarios (CRUD & Pila Dinámica)", font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO)
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

        e_id_user = ctk.CTkEntry(frame_form, placeholder_text="ID (ej: U6)", width=100, corner_radius=10)
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

            nuevo_usr = Usuario(id_u, nombre_u)

            def undo():
                lista_usuarios.eliminar_por_id(id_u, tipo="usuario")

            def redo():
                lista_usuarios.agregar(nuevo_usr)

            pila_historial.registrar_y_ejecutar(f"Agregar Usuario: {nombre_u}", undo, redo)
            messagebox.showinfo("Éxito", f"Usuario '{nombre_u}' registrado.")
            self.vista_usuarios()

        btn_add_u = ctk.CTkButton(frame_form, text="➕ Agregar", fg_color=COLOR_AZUL_CIELO, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, width=95, command=agregar_usuario)
        btn_add_u.grid(row=0, column=2, padx=5, pady=12)

        self.mostrar_tabla_usuarios(row=3)

    def vista_prestamos(self):
        self.limpiar_panel()
        lbl_titulo = ctk.CTkLabel(self.panel_contenido, text="🔄 Préstamos & Multas", font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO)
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
                messagebox.showwarning("Validación", "Selecciona usuario y título.")
                return

            libro_en_arbol = arbol_libros.buscar(titulo_sel)
            if not libro_en_arbol:
                messagebox.showerror("Error", f"El libro '{titulo_sel}' no existe en el catálogo del Árbol BST.")
                return

            nuevo_id_p = f"P{len(lista_prestamos.a_lista()) + 1}"
            nuevo_p = Prestamo(nuevo_id_p, usuario_sel, libro_en_arbol.titulo, "PRESTADO")

            def undo():
                lista_prestamos.eliminar_por_id(nuevo_id_p, tipo="prestamo")

            def redo():
                lista_prestamos.agregar(nuevo_p)

            pila_historial.registrar_y_ejecutar(f"Préstamo {nuevo_id_p} a {usuario_sel}", undo, redo)
            messagebox.showinfo("Éxito", f"Préstamo '{nuevo_id_p}' asignado.")
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
                messagebox.showwarning("Validación", "Ingresa ID válido y días en número entero.")
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
                prestamo_obj.estado = estado_viejo
                if usr_obj:
                    usr_obj.multa_acumulada = multa_anterior

            def redo():
                prestamo_obj.estado = "DEVUELTO"
                if usr_obj and multa_generada > 0:
                    usr_obj.multa_acumulada += multa_generada

            pila_historial.registrar_y_ejecutar(f"Devolución de {id_p}", undo, redo)
            self.vista_prestamos()

        btn_dev = ctk.CTkButton(frame_dev, text="🔄 Devolver Libro", fg_color=COLOR_MORADO_SUAVE, hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, command=devolver)
        btn_dev.grid(row=0, column=2, padx=10, pady=10)

        lbl_tabla_p = ctk.CTkLabel(self.panel_contenido, text="📋 Registro de Préstamos", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXTO)
        lbl_tabla_p.grid(row=3, column=0, sticky="w", pady=(5, 5))
        self.mostrar_tabla_prestamos(row=4)

        lbl_deudas = ctk.CTkLabel(self.panel_contenido, text="💰 Control de Multas por Usuario", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXTO)
        lbl_deudas.grid(row=5, column=0, sticky="w", pady=(10, 5))
        self.mostrar_tabla_usuarios(row=6)

    def vista_historial(self):
        self.limpiar_panel()
        lbl_titulo = ctk.CTkLabel(self.panel_contenido, text="📜 Historial General de Operaciones (Pila Dinámica)", font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO)
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        frame_acciones = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=14)
        frame_acciones.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        def ejecutar_deshacer():
            desc = pila_historial.deshacer()
            if desc:
                messagebox.showinfo("Deshacer", f"Se deshizo: '{desc}'")
                self.vista_historial()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para deshacer en la Pila.")

        def ejecutar_rehacer():
            desc = pila_historial.rehacer()
            if desc:
                messagebox.showinfo("Rehacer", f"Se rehizo: '{desc}'")
                self.vista_historial()
            else:
                messagebox.showwarning("Aviso", "No hay acciones para rehacer en la Pila.")

        btn_u = ctk.CTkButton(frame_acciones, text="↩️ Deshacer Última Acción", fg_color=COLOR_MORADO_SUAVE, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, command=ejecutar_deshacer)
        btn_u.pack(side="left", padx=15, pady=10)
        btn_r = ctk.CTkButton(frame_acciones, text="🔁 Rehacer Acción", fg_color=COLOR_AZUL_CIELO, text_color=COLOR_TEXTO, hover_color=COLOR_AZUL_HOVER, command=ejecutar_rehacer)
        btn_r.pack(side="left", padx=10, pady=10)

        frame_lista = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_lista.grid(row=2, column=0, sticky="nsew", pady=(0, 10))

        lbl_top = ctk.CTkLabel(frame_lista, text="Pila de Historial Dinámica (Cima / Más reciente arriba):", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXTO)
        lbl_top.pack(anchor="w", padx=15, pady=(10, 5))

        historial = pila_historial.obtener_todas()
        if not historial:
            lbl_vacio = ctk.CTkLabel(frame_lista, text="No hay operaciones registradas en la Pila aún.", text_color=COLOR_TEXTO_SUAVE)
            lbl_vacio.pack(padx=15, pady=15)
        else:
            for i, desc in enumerate(historial, start=1):
                lbl_item = ctk.CTkLabel(frame_lista, text=f"{i}. 📌 {desc}", font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO, anchor="w")
                lbl_item.pack(fill="x", padx=20, pady=3)

# ==========================================
# INICIALIZACIÓN DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    app = AppBiblioteca()
    app.mainloop()