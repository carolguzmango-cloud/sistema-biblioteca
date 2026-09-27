import customtkinter as ctk
from tkinter import ttk, messagebox

# ==============================================================================
# UNIDAD 1 & 2: ESTRUCTURAS DE DATOS Y POO
# ==============================================================================

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

# Lista Doblemente Enlazada (Unidad 2)
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
        """Inserta un libro ordenado alfabéticamente por título automáticamente."""
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
        """Inserta un usuario ordenado alfabéticamente por nombre automáticamente."""
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

    def a_lista(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    # Algoritmo de Ordenación por Método Burbuja (Unidad 1)
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

# ==============================================================================
# INTERFAZ GRÁFICA (CustomTkinter)
# ==============================================================================
ctk.set_appearance_mode("Light")

COLOR_FONDO = "#F4F0EA"
COLOR_PANEL = "#FFFFFF"
COLOR_SIDEBAR = "#E2D4F0"       # Morado claro / Lavanda
COLOR_TEXTO = "#3A3042"
COLOR_TEXTO_SUAVE = "#705D82"

COLOR_AZUL_CIELO = "#A0C4FF"    # Azul cielo
COLOR_AZUL_HOVER = "#80B3FF"
COLOR_MORADO_SUAVE = "#C8B6E2"
COLOR_TARJETA_AZUL = "#B9F3FC"

class AppBiblioteca(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✨ Sistema de Gestión de Biblioteca - Unidad 2 ✨")
        self.geometry("1100x750")
        self.configure(fg_color=COLOR_FONDO)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.configurar_estilos_tabla()
        self.crear_sidebar()

        self.panel_contenido = ctk.CTkFrame(self, fg_color="transparent")
        self.panel_contenido.grid(row=0, column=1, sticky="nsew", padx=25, pady=25)
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
            sidebar, text="Estructuras de Datos", 
            font=ctk.CTkFont(size=12), text_color=COLOR_TEXTO_SUAVE
        )
        lbl_sub.grid(row=1, column=0, padx=20, pady=(0, 25))

        opciones = [
            ("🏠  Panel Principal", self.vista_dashboard),
            ("📖  Catálogo Libros", self.vista_libros),
            ("👥  Gestión Usuarios", self.vista_usuarios),
            ("🔄  Préstamos & Multas", self.vista_prestamos)
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

    # --------------------------------------------------------------------------
    # VISTA 1: DASHBOARD
    # --------------------------------------------------------------------------
    def vista_dashboard(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="¡Bienvenida al Panel de Control! ✨", 
            font=ctk.CTkFont(size=25, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Regla de préstamos
        frame_regla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_SIDEBAR, corner_radius=12)
        frame_regla.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        lbl_regla = ctk.CTkLabel(
            frame_regla, 
            text="📌 REGLA DE PRÉSTAMOS: El tiempo máximo es de 7 DÍAS. Transcurrido este plazo, se cobra una multa automática de $1,000 por cada día de mora.",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=COLOR_TEXTO, wraplength=750, justify="left"
        )
        lbl_regla.pack(padx=15, pady=10)

        # Tarjetas KPIs
        frame_kpis = ctk.CTkFrame(self.panel_contenido, fg_color="transparent")
        frame_kpis.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        frame_kpis.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="kpi")

        prestamos_activos = sum(1 for p in lista_prestamos.a_lista() if p.estado == "PRESTADO")
        multa_total_sistema = sum(u.multa_acumulada for u in lista_usuarios.a_lista())

        self.crear_tarjeta_kpi(frame_kpis, 0, "Préstamos Activos", str(prestamos_activos), "📖", COLOR_TARJETA_AZUL)
        self.crear_tarjeta_kpi(frame_kpis, 1, "Libros Registrados", str(len(lista_libros.a_lista())), "📚", COLOR_MORADO_SUAVE)
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

        lbl_v = ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=22, weight="bold"), text_color=COLOR_TEXTO)
        lbl_v.pack(anchor="w", padx=12, pady=(0, 0))

        lbl_t = ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=11, weight="bold"), text_color=COLOR_TEXTO_SUAVE)
        lbl_t.pack(anchor="w", padx=12, pady=(0, 8))

    # --------------------------------------------------------------------------
    # VISTA 2: LIBROS
    # --------------------------------------------------------------------------
    def vista_libros(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="📖 Catálogo de Libros", 
            font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 15))

        frame_form = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_form.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        e_id = ctk.CTkEntry(frame_form, placeholder_text="ID / ISBN", width=110, corner_radius=10)
        e_id.grid(row=0, column=0, padx=10, pady=15)

        e_tit = ctk.CTkEntry(frame_form, placeholder_text="Título del Libro", width=200, corner_radius=10)
        e_tit.grid(row=0, column=1, padx=10, pady=15)

        e_aut = ctk.CTkEntry(frame_form, placeholder_text="Autor", width=180, corner_radius=10)
        e_aut.grid(row=0, column=2, padx=10, pady=15)

        def agregar():
            id_val = e_id.get().strip()
            tit_val = e_tit.get().strip()
            aut_val = e_aut.get().strip()

            if not id_val or not tit_val or not aut_val:
                messagebox.showwarning("Validación", "Por favor completa todos los campos.")
                return

            if any(l.id_libro == id_val for l in lista_libros.a_lista()):
                messagebox.showerror("Error", f"El ID '{id_val}' ya existe.")
                return

            # Inserta ordenado alfabéticamente de forma automática
            lista_libros.agregar_ordenado_libro(Libro(id_val, tit_val, aut_val))
            messagebox.showinfo("Éxito", "Libro registrado y ordenado alfabéticamente correctamente.")
            self.vista_libros()

        def ordenar():
            lista_libros.ordenar_por_titulo()
            messagebox.showinfo("Ordenación", "Catálogo ordenado alfabéticamente por Título (Bubble Sort).")
            self.vista_libros()

        btn_add = ctk.CTkButton(
            frame_form, text="➕ Agregar", fg_color=COLOR_AZUL_CIELO, 
            hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, 
            font=ctk.CTkFont(size=12, weight="bold"), corner_radius=12, command=agregar
        )
        btn_add.grid(row=0, column=3, padx=5, pady=15)

        btn_ord = ctk.CTkButton(
            frame_form, text="🔤 Ordenar A-Z", fg_color=COLOR_MORADO_SUAVE, 
            hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, 
            font=ctk.CTkFont(size=12, weight="bold"), corner_radius=12, command=ordenar
        )
        btn_ord.grid(row=0, column=4, padx=5, pady=15)

        self.mostrar_tabla_libros(row=2)

    # --------------------------------------------------------------------------
    # VISTA 3: USUARIOS
    # --------------------------------------------------------------------------
    def vista_usuarios(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="👥 Gestión de Usuarios", 
            font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 15))

        frame_form = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_form.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        e_id_user = ctk.CTkEntry(frame_form, placeholder_text="ID Usuario (ej: U4)", width=160, corner_radius=10)
        e_id_user.grid(row=0, column=0, padx=15, pady=15)

        e_nombre = ctk.CTkEntry(frame_form, placeholder_text="Nombre Completo", width=280, corner_radius=10)
        e_nombre.grid(row=0, column=1, padx=15, pady=15)

        def agregar_usuario():
            id_u = e_id_user.get().strip()
            nombre_u = e_nombre.get().strip()

            if not id_u or not nombre_u:
                messagebox.showwarning("Validación", "Debes ingresar ID y Nombre del usuario.")
                return

            if any(u.id_usuario == id_u for u in lista_usuarios.a_lista()):
                messagebox.showerror("Error", f"El ID de usuario '{id_u}' ya existe.")
                return

            # Inserta ordenado alfabéticamente de forma automática
            lista_usuarios.agregar_ordenado_usuario(Usuario(id_u, nombre_u))
            messagebox.showinfo("Éxito", f"Usuario '{nombre_u}' registrado y ordenado alfabéticamente.")
            self.vista_usuarios()

        btn_add_u = ctk.CTkButton(
            frame_form, text="👤 Agregar Usuario", fg_color=COLOR_AZUL_CIELO, 
            hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, 
            font=ctk.CTkFont(size=13, weight="bold"), corner_radius=12, command=agregar_usuario
        )
        btn_add_u.grid(row=0, column=2, padx=15, pady=15)

        frame_tabla = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_tabla.grid(row=2, column=0, sticky="nsew")

        tree = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Deuda"), show="headings")
        tree.heading("ID", text="ID Usuario")
        tree.heading("Nombre", text="Nombre Completo")
        tree.heading("Deuda", text="Multa Acumulada")

        tree.column("ID", width=120)
        tree.column("Nombre", width=320)
        tree.column("Deuda", width=150)
        
        for u in lista_usuarios.a_lista():
            tree.insert("", "end", values=(u.id_usuario, u.nombre, f"${u.multa_acumulada}"))

        tree.pack(fill="both", expand=True, padx=15, pady=15)

    # --------------------------------------------------------------------------
    # VISTA 4: PRÉSTAMOS, MULTAS Y ESTADOS
    # --------------------------------------------------------------------------
    def vista_prestamos(self):
        self.limpiar_panel()

        lbl_titulo = ctk.CTkLabel(
            self.panel_contenido, text="🔄 Préstamos & Multas", 
            font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # --- SECCIÓN 1: SOLICITAR PRÉSTAMO POR TÍTULO ---
        frame_nuevo_p = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_nuevo_p.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        nombres_usuarios = [u.nombre for u in lista_usuarios.a_lista()]
        if not nombres_usuarios:
            nombres_usuarios = ["Sin usuarios"]

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
                messagebox.showerror("Error", f"El libro '{titulo_sel}' no existe en el catálogo.")
                return

            nuevo_id_p = f"P{len(lista_prestamos.a_lista()) + 1}"
            lista_prestamos.agregar(Prestamo(nuevo_id_p, usuario_sel, libro_existente.titulo, "PRESTADO"))
            messagebox.showinfo("Éxito", f"Préstamo '{nuevo_id_p}' asignado a {usuario_sel}.\nEstado: PRESTADO")
            self.vista_prestamos()

        btn_p = ctk.CTkButton(
            frame_nuevo_p, text="📖 Solicitar Préstamo", fg_color=COLOR_AZUL_CIELO, 
            hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, 
            font=ctk.CTkFont(size=12, weight="bold"), corner_radius=12, command=registrar_prestamo
        )
        btn_p.grid(row=0, column=2, padx=10, pady=10)

        # --- SECCIÓN 2: DEVOLUCIÓN ---
        frame_dev = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_dev.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        e_id_p = ctk.CTkEntry(frame_dev, placeholder_text="ID Préstamo (ej: P1)", width=140, corner_radius=10)
        e_id_p.grid(row=0, column=0, padx=10, pady=10)

        e_dias = ctk.CTkEntry(frame_dev, placeholder_text="Días prestado (ej: 9)", width=140, corner_radius=10)
        e_dias.grid(row=0, column=1, padx=10, pady=10)

        def devolver():
            id_p = e_id_p.get().strip()
            dias_str = e_dias.get().strip()

            if not id_p or not dias_str:
                messagebox.showwarning("Validación", "Por favor completa los campos para la devolución.")
                return

            if not dias_str.isdigit():
                messagebox.showerror("Error", "Los días deben ser un número entero.")
                return

            dias = int(dias_str)
            prestamo_obj = next((p for p in lista_prestamos.a_lista() if p.id_prestamo == id_p), None)

            if not prestamo_obj:
                messagebox.showerror("Error", f"No se encontró el préstamo '{id_p}'.")
                return

            # Cambio de Estado a DEVUELTO
            prestamo_obj.estado = "DEVUELTO"
            
            # $1,000 por día adicional a partir del día 8
            multa_generada = (dias - 7) * 1000 if dias > 7 else 0

            usr_obj = next((u for u in lista_usuarios.a_lista() if u.nombre == prestamo_obj.usuario_nombre), None)
            if usr_obj and multa_generada > 0:
                usr_obj.multa_acumulada += multa_generada
                messagebox.showwarning(
                    "Devolución con Multa", 
                    f"¡Libro Devuelto!\n\nDías con el libro: {dias} días.\nMulta acumulada: ${multa_generada} cargada a {usr_obj.nombre}."
                )
            else:
                messagebox.showinfo("Devolución Exitosa", f"¡Libro Devuelto a tiempo ({dias} días)!\nEstado actualizado a DEVUELTO.")

            self.vista_prestamos()

        btn_dev = ctk.CTkButton(
            frame_dev, text="🔄 Devolver Libro", fg_color=COLOR_MORADO_SUAVE, 
            hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, 
            font=ctk.CTkFont(size=12, weight="bold"), corner_radius=12, command=devolver
        )
        btn_dev.grid(row=0, column=2, padx=10, pady=10)

        # --- SECCIÓN 3: TABLA CON TÍTULO DEL LIBRO Y ESTADO (PRESTADO / DEVUELTO) ---
        lbl_tabla_p = ctk.CTkLabel(
            self.panel_contenido, text="📋 Registro de Préstamos (Título de Libro y Estado)", 
            font=ctk.CTkFont(size=15, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_tabla_p.grid(row=3, column=0, sticky="w", pady=(5, 5))

        self.mostrar_tabla_prestamos(row=4)

        # --- SECCIÓN 4: PAGO DE MULTAS DE USUARIOS ---
        lbl_deudas = ctk.CTkLabel(
            self.panel_contenido, text="💰 Control de Multas por Usuario", 
            font=ctk.CTkFont(size=15, weight="bold"), text_color=COLOR_TEXTO
        )
        lbl_deudas.grid(row=5, column=0, sticky="w", pady=(10, 5))

        frame_pago = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_pago.grid(row=6, column=0, sticky="ew", pady=(0, 10))

        cb_usuario_pago = ctk.CTkComboBox(frame_pago, values=nombres_usuarios, width=200, corner_radius=10)
        cb_usuario_pago.grid(row=0, column=0, padx=15, pady=10)

        def pagar_multa():
            usr_nombre = cb_usuario_pago.get().strip()
            usr = next((u for u in lista_usuarios.a_lista() if u.nombre == usr_nombre), None)

            if not usr:
                messagebox.showerror("Error", "Usuario no encontrado.")
                return

            if usr.multa_acumulada == 0:
                messagebox.showinfo("Sin Deuda", f"El usuario {usr.nombre} no debe nada (Saldo: $0).")
            else:
                m_anterior = usr.multa_acumulada
                usr.multa_acumulada = 0
                messagebox.showinfo("Pago Exitoso", f"Pago recibido: ${m_anterior} de {usr.nombre}.\n\nEstado actual: NO DEBE ($0).")
                self.vista_prestamos()

        btn_pagar = ctk.CTkButton(
            frame_pago, text="💳 Pagar Multa (Dejar en $0)", fg_color=COLOR_AZUL_CIELO, 
            hover_color=COLOR_AZUL_HOVER, text_color=COLOR_TEXTO, 
            font=ctk.CTkFont(size=12, weight="bold"), corner_radius=12, command=pagar_multa
        )
        btn_pagar.grid(row=0, column=1, padx=15, pady=10)

        # Tabla de Estado Financiero por Usuario
        frame_tabla_m = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame_tabla_m.grid(row=7, column=0, sticky="nsew")

        tree_m = ttk.Treeview(frame_tabla_m, columns=("Usuario", "Estado", "Multa"), show="headings", height=3)
        tree_m.heading("Usuario", text="Usuario")
        tree_m.heading("Estado", text="Estado de Cuenta")
        tree_m.heading("Multa", text="Saldo Acumulado")

        tree_m.column("Usuario", width=220)
        tree_m.column("Estado", width=180)
        tree_m.column("Multa", width=180)

        for u in lista_usuarios.a_lista():
            estado_txt = "🔴 DEBE MULTA" if u.multa_acumulada > 0 else "🟢 NO DEBE ($0)"
            tree_m.insert("", "end", values=(u.nombre, estado_txt, f"${u.multa_acumulada}"))

        tree_m.pack(fill="both", expand=True, padx=15, pady=8)

    # --------------------------------------------------------------------------
    # TABLAS AUXILIARES
    # --------------------------------------------------------------------------
    def mostrar_tabla_libros(self, row):
        frame = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame.grid(row=row, column=0, sticky="nsew")

        tree = ttk.Treeview(frame, columns=("ID", "Título", "Autor"), show="headings")
        tree.heading("ID", text="ID / ISBN")
        tree.heading("Título", text="Título")
        tree.heading("Autor", text="Autor")

        tree.column("ID", width=100)
        tree.column("Título", width=320)
        tree.column("Autor", width=200)

        for l in lista_libros.a_lista():
            tree.insert("", "end", values=(l.id_libro, l.titulo, l.autor))

        tree.pack(fill="both", expand=True, padx=15, pady=15)

    def mostrar_tabla_prestamos(self, row):
        frame = ctk.CTkFrame(self.panel_contenido, fg_color=COLOR_PANEL, corner_radius=16)
        frame.grid(row=row, column=0, sticky="nsew")

        tree = ttk.Treeview(frame, columns=("ID", "Usuario", "Libro", "Estado"), show="headings", height=4)
        tree.heading("ID", text="ID Préstamo")
        tree.heading("Usuario", text="Usuario")
        tree.heading("Libro", text="Título del Libro")
        tree.heading("Estado", text="Estado del Préstamo")

        tree.column("ID", width=100)
        tree.column("Usuario", width=180)
        tree.column("Libro", width=280)
        tree.column("Estado", width=140)

        for p in lista_prestamos.a_lista():
            tree.insert("", "end", values=(p.id_prestamo, p.usuario_nombre, p.libro_titulo, p.estado))

        tree.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = AppBiblioteca()
    app.mainloop()