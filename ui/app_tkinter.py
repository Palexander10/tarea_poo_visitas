"""
Módulo: ui/app_tkinter.py
Descripción: Capa de interfaz gráfica construida con Tkinter.
             Recibe el servicio por inyección de dependencias y
             no contiene lógica de negocio propia.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from servicios.visita_servicio import VisitaServicio


# ──────────────────────────────────────────────────────────────
# Paleta de colores y constantes de estilo
# ──────────────────────────────────────────────────────────────
COLORES = {
    "fondo_principal": "#F0F4F8",
    "fondo_header":    "#1A2E4A",
    "fondo_formulario":"#FFFFFF",
    "fondo_tabla":     "#FFFFFF",
    "acento_azul":     "#2563EB",
    "acento_rojo":     "#DC2626",
    "acento_gris":     "#6B7280",
    "texto_claro":     "#FFFFFF",
    "texto_oscuro":    "#111827",
    "texto_etiqueta":  "#374151",
    "borde":           "#D1D5DB",
    "hover_azul":      "#1D4ED8",
    "hover_rojo":      "#B91C1C",
    "fila_par":        "#F9FAFB",
    "fila_impar":      "#FFFFFF",
    "seleccion":       "#DBEAFE",
}

FUENTE_TITULO    = ("Segoe UI", 18, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 10)
FUENTE_LABEL     = ("Segoe UI", 10, "bold")
FUENTE_ENTRY     = ("Segoe UI", 10)
FUENTE_BOTON     = ("Segoe UI", 10, "bold")
FUENTE_TABLA_CAB = ("Segoe UI", 10, "bold")
FUENTE_TABLA     = ("Segoe UI", 10)
FUENTE_ESTADO    = ("Segoe UI", 9)


class AppTkinter:
    """
    Clase principal de la interfaz gráfica del Sistema de Registro de Visitantes.

    Aplica:
        - Inyección de dependencias: recibe VisitaServicio en el constructor.
        - Separación de responsabilidades: solo gestiona la UI, delega lógica al servicio.
        - Composición: construye la interfaz mediante métodos privados especializados.
    """

    def __init__(self, servicio: VisitaServicio) -> None:
        """
        Constructor de la interfaz gráfica.

        Args:
            servicio (VisitaServicio): Servicio inyectado con la lógica CRUD.
        """
        self._servicio = servicio

        # Ventana raíz
        self._root = tk.Tk()
        self._configurar_ventana()

        # Variables de los campos del formulario
        self._var_cedula  = tk.StringVar()
        self._var_nombre  = tk.StringVar()
        self._var_motivo  = tk.StringVar()

        # Construcción de la interfaz por secciones
        self._construir_header()
        self._construir_cuerpo()
        self._construir_barra_estado()

    # ──────────────────────────────────────────
    # Configuración de la ventana
    # ──────────────────────────────────────────

    def _configurar_ventana(self) -> None:
        """Establece las propiedades generales de la ventana principal."""
        self._root.title("Sistema de Registro de Visitantes")
        self._root.geometry("820x620")
        self._root.minsize(700, 550)
        self._root.configure(bg=COLORES["fondo_principal"])
        self._root.resizable(True, True)

        # Centrar en pantalla
        self._root.update_idletasks()
        ancho  = self._root.winfo_width()
        alto   = self._root.winfo_height()
        x = (self._root.winfo_screenwidth()  - ancho) // 2
        y = (self._root.winfo_screenheight() - alto)  // 2
        self._root.geometry(f"+{x}+{y}")

    # ──────────────────────────────────────────
    # Sección: Header
    # ──────────────────────────────────────────

    def _construir_header(self) -> None:
        """Construye la barra de encabezado con el título de la aplicación."""
        frame_header = tk.Frame(
            self._root,
            bg=COLORES["fondo_header"],
            pady=16
        )
        frame_header.pack(fill=tk.X)

        tk.Label(
            frame_header,
            text="🏢  Sistema de Registro de Visitantes",
            font=FUENTE_TITULO,
            fg=COLORES["texto_claro"],
            bg=COLORES["fondo_header"]
        ).pack()

        tk.Label(
            frame_header,
            text="Gestión de acceso a la oficina  •  CRUD en memoria",
            font=FUENTE_SUBTITULO,
            fg="#94A3B8",
            bg=COLORES["fondo_header"]
        ).pack(pady=(2, 0))

    # ──────────────────────────────────────────
    # Sección: Cuerpo principal
    # ──────────────────────────────────────────

    def _construir_cuerpo(self) -> None:
        """Construye el cuerpo principal dividiéndolo en panel izquierdo y tabla."""
        frame_cuerpo = tk.Frame(self._root, bg=COLORES["fondo_principal"])
        frame_cuerpo.pack(fill=tk.BOTH, expand=True, padx=16, pady=16)

        frame_cuerpo.columnconfigure(0, weight=0)
        frame_cuerpo.columnconfigure(1, weight=1)
        frame_cuerpo.rowconfigure(0, weight=1)

        self._construir_panel_formulario(frame_cuerpo)
        self._construir_panel_tabla(frame_cuerpo)

    def _construir_panel_formulario(self, padre: tk.Frame) -> None:
        """
        Construye el panel izquierdo con el formulario y los botones de acción.

        Args:
            padre (tk.Frame): Frame contenedor padre.
        """
        frame_izq = tk.Frame(
            padre,
            bg=COLORES["fondo_formulario"],
            bd=0,
            relief=tk.FLAT,
            width=270
        )
        frame_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        frame_izq.grid_propagate(False)
        frame_izq.pack_propagate(False)

        # ── Título del formulario ──
        tk.Label(
            frame_izq,
            text="Nuevo Visitante",
            font=("Segoe UI", 13, "bold"),
            fg=COLORES["fondo_header"],
            bg=COLORES["fondo_formulario"]
        ).pack(anchor="w", padx=20, pady=(20, 4))

        tk.Frame(frame_izq, bg=COLORES["acento_azul"], height=3).pack(
            fill=tk.X, padx=20, pady=(0, 16)
        )

        # ── Campos del formulario ──
        self._agregar_campo(frame_izq, "Cédula *", self._var_cedula,  "Ej: 1104567890")
        self._agregar_campo(frame_izq, "Nombre completo *", self._var_nombre, "Ej: María García")
        self._agregar_campo(frame_izq, "Motivo de visita *", self._var_motivo, "Ej: Reunión de trabajo")

        # ── Botones de acción ──
        frame_botones = tk.Frame(frame_izq, bg=COLORES["fondo_formulario"])
        frame_botones.pack(fill=tk.X, padx=20, pady=(24, 0))

        self._crear_boton(
            frame_botones,
            texto="✔  Registrar Visitante",
            color_fondo=COLORES["acento_azul"],
            color_hover=COLORES["hover_azul"],
            comando=self._accion_registrar
        ).pack(fill=tk.X, pady=(0, 8))

        self._crear_boton(
            frame_botones,
            texto="✖  Eliminar Seleccionado",
            color_fondo=COLORES["acento_rojo"],
            color_hover=COLORES["hover_rojo"],
            comando=self._accion_eliminar
        ).pack(fill=tk.X, pady=(0, 8))

        self._crear_boton(
            frame_botones,
            texto="↺  Limpiar Campos",
            color_fondo=COLORES["acento_gris"],
            color_hover="#4B5563",
            comando=self._accion_limpiar
        ).pack(fill=tk.X)

    def _agregar_campo(
        self,
        padre: tk.Frame,
        etiqueta: str,
        variable: tk.StringVar,
        placeholder: str
    ) -> None:
        """
        Agrega un campo de texto con su etiqueta al formulario.

        Args:
            padre     : Frame contenedor.
            etiqueta  : Texto de la etiqueta.
            variable  : StringVar vinculada al campo.
            placeholder: Texto de ayuda (placeholder).
        """
        tk.Label(
            padre,
            text=etiqueta,
            font=FUENTE_LABEL,
            fg=COLORES["texto_etiqueta"],
            bg=COLORES["fondo_formulario"]
        ).pack(anchor="w", padx=20, pady=(0, 4))

        frame_entry = tk.Frame(padre, bg=COLORES["borde"], padx=1, pady=1)
        frame_entry.pack(fill=tk.X, padx=20, pady=(0, 12))

        entry = tk.Entry(
            frame_entry,
            textvariable=variable,
            font=FUENTE_ENTRY,
            fg=COLORES["texto_oscuro"],
            bg=COLORES["fondo_formulario"],
            relief=tk.FLAT,
            bd=6
        )
        entry.pack(fill=tk.X)

        # Placeholder visual
        self._configurar_placeholder(entry, variable, placeholder)

    def _configurar_placeholder(
        self,
        entry: tk.Entry,
        variable: tk.StringVar,
        placeholder: str
    ) -> None:
        """
        Configura el comportamiento de placeholder en un Entry.

        Args:
            entry      : Widget Entry a configurar.
            variable   : StringVar asociada.
            placeholder: Texto del placeholder.
        """
        COLOR_PLACEHOLDER = "#9CA3AF"
        COLOR_NORMAL      = COLORES["texto_oscuro"]

        def al_enfocar(_event=None):
            if variable.get() == placeholder:
                variable.set("")
                entry.configure(fg=COLOR_NORMAL)

        def al_desenfocar(_event=None):
            if not variable.get():
                variable.set(placeholder)
                entry.configure(fg=COLOR_PLACEHOLDER)

        variable.set(placeholder)
        entry.configure(fg=COLOR_PLACEHOLDER)
        entry.bind("<FocusIn>",  al_enfocar)
        entry.bind("<FocusOut>", al_desenfocar)

        # Guardar placeholder para validación posterior
        entry._placeholder = placeholder  # type: ignore[attr-defined]

    def _crear_boton(
        self,
        padre: tk.Widget,
        texto: str,
        color_fondo: str,
        color_hover: str,
        comando
    ) -> tk.Button:
        """
        Crea y retorna un botón estilizado con efecto hover.

        Args:
            padre      : Widget padre.
            texto      : Texto del botón.
            color_fondo: Color de fondo normal.
            color_hover: Color de fondo al pasar el mouse.
            comando    : Función a ejecutar al hacer clic.

        Returns:
            tk.Button: Botón configurado (sin empaquetar).
        """
        boton = tk.Button(
            padre,
            text=texto,
            font=FUENTE_BOTON,
            fg=COLORES["texto_claro"],
            bg=color_fondo,
            activebackground=color_hover,
            activeforeground=COLORES["texto_claro"],
            relief=tk.FLAT,
            bd=0,
            padx=12,
            pady=9,
            cursor="hand2",
            command=comando
        )
        boton.bind("<Enter>", lambda _e: boton.configure(bg=color_hover))
        boton.bind("<Leave>", lambda _e: boton.configure(bg=color_fondo))
        return boton

    # ──────────────────────────────────────────
    # Sección: Panel de tabla
    # ──────────────────────────────────────────

    def _construir_panel_tabla(self, padre: tk.Frame) -> None:
        """
        Construye el panel derecho con la tabla de visitantes.

        Args:
            padre (tk.Frame): Frame contenedor padre.
        """
        frame_der = tk.Frame(
            padre,
            bg=COLORES["fondo_tabla"],
            bd=0
        )
        frame_der.grid(row=0, column=1, sticky="nsew")

        # ── Título de la tabla ──
        frame_titulo = tk.Frame(frame_der, bg=COLORES["fondo_tabla"])
        frame_titulo.pack(fill=tk.X, padx=20, pady=(20, 8))

        tk.Label(
            frame_titulo,
            text="Visitantes Registrados",
            font=("Segoe UI", 13, "bold"),
            fg=COLORES["fondo_header"],
            bg=COLORES["fondo_tabla"]
        ).pack(side=tk.LEFT)

        self._lbl_contador = tk.Label(
            frame_titulo,
            text="0 registros",
            font=FUENTE_ESTADO,
            fg=COLORES["acento_azul"],
            bg=COLORES["fondo_tabla"]
        )
        self._lbl_contador.pack(side=tk.RIGHT)

        tk.Frame(frame_der, bg=COLORES["acento_azul"], height=3).pack(
            fill=tk.X, padx=20, pady=(0, 12)
        )

        # ── Treeview ──
        frame_tabla = tk.Frame(frame_der, bg=COLORES["fondo_tabla"])
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        self._tabla = self._crear_treeview(frame_tabla)

    def _crear_treeview(self, padre: tk.Frame) -> ttk.Treeview:
        """
        Crea y configura el widget Treeview con su scrollbar.

        Args:
            padre (tk.Frame): Frame contenedor.

        Returns:
            ttk.Treeview: Tabla configurada.
        """
        # Estilo de la tabla
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Visitantes.Treeview",
            background=COLORES["fondo_tabla"],
            foreground=COLORES["texto_oscuro"],
            rowheight=32,
            fieldbackground=COLORES["fondo_tabla"],
            font=FUENTE_TABLA,
            borderwidth=0
        )
        estilo.configure(
            "Visitantes.Treeview.Heading",
            background=COLORES["fondo_header"],
            foreground=COLORES["texto_claro"],
            font=FUENTE_TABLA_CAB,
            relief=tk.FLAT,
            padding=(8, 6)
        )
        estilo.map(
            "Visitantes.Treeview",
            background=[("selected", COLORES["seleccion"])],
            foreground=[("selected", COLORES["texto_oscuro"])]
        )

        columnas = ("#", "cedula", "nombre", "motivo")
        tabla = ttk.Treeview(
            padre,
            columns=columnas,
            show="headings",
            style="Visitantes.Treeview",
            selectmode="browse"
        )

        # Definir encabezados
        tabla.heading("#",      text="#",               anchor=tk.CENTER)
        tabla.heading("cedula", text="Cédula",          anchor=tk.W)
        tabla.heading("nombre", text="Nombre Completo", anchor=tk.W)
        tabla.heading("motivo", text="Motivo de Visita",anchor=tk.W)

        # Definir anchos de columna
        tabla.column("#",      width=40,  minwidth=40,  anchor=tk.CENTER, stretch=False)
        tabla.column("cedula", width=120, minwidth=100, anchor=tk.W)
        tabla.column("nombre", width=180, minwidth=120, anchor=tk.W)
        tabla.column("motivo", width=200, minwidth=120, anchor=tk.W, stretch=True)

        # Etiquetas para filas alternas
        tabla.tag_configure("par",   background=COLORES["fila_par"])
        tabla.tag_configure("impar", background=COLORES["fila_impar"])

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(padre, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscrollcommand=scrollbar.set)

        tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        return tabla

    # ──────────────────────────────────────────
    # Sección: Barra de estado
    # ──────────────────────────────────────────

    def _construir_barra_estado(self) -> None:
        """Construye la barra de estado inferior de la aplicación."""
        frame_estado = tk.Frame(
            self._root,
            bg=COLORES["fondo_header"],
            pady=6
        )
        frame_estado.pack(fill=tk.X, side=tk.BOTTOM)

        self._lbl_estado = tk.Label(
            frame_estado,
            text="✔  Sistema listo. Complete el formulario para registrar un visitante.",
            font=FUENTE_ESTADO,
            fg="#94A3B8",
            bg=COLORES["fondo_header"]
        )
        self._lbl_estado.pack(side=tk.LEFT, padx=16)

        tk.Label(
            frame_estado,
            text="POO · Arquitectura Modular por Capas",
            font=FUENTE_ESTADO,
            fg="#475569",
            bg=COLORES["fondo_header"]
        ).pack(side=tk.RIGHT, padx=16)

    # ──────────────────────────────────────────
    # Acciones de los botones (manejadores)
    # ──────────────────────────────────────────

    def _accion_registrar(self) -> None:
        """Maneja el evento del botón 'Registrar Visitante'."""
        cedula = self._leer_campo(self._var_cedula)
        nombre = self._leer_campo(self._var_nombre)
        motivo = self._leer_campo(self._var_motivo)

        try:
            self._servicio.registrar(cedula, nombre, motivo)
            self._actualizar_tabla()
            self._accion_limpiar()
            self._actualizar_estado(
                f"✔  Visitante '{nombre}' registrado correctamente.",
                color="#4ADE80"
            )
            messagebox.showinfo(
                "Registro exitoso",
                f"✔ Visitante registrado correctamente.\n\n"
                f"  Cédula : {cedula}\n"
                f"  Nombre : {nombre}\n"
                f"  Motivo : {motivo}"
            )
        except ValueError as error:
            self._actualizar_estado(f"⚠  {error}", color="#FCA5A5")
            messagebox.showwarning("Error de validación", str(error))

    def _accion_eliminar(self) -> None:
        """Maneja el evento del botón 'Eliminar Seleccionado'."""
        seleccion = self._tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Por favor, seleccione un visitante de la tabla para eliminarlo."
            )
            return

        item   = self._tabla.item(seleccion[0])
        cedula = item["values"][1]
        nombre = item["values"][2]

        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar el registro de:\n\n"
            f"  Nombre : {nombre}\n"
            f"  Cédula : {cedula}\n\n"
            "Esta acción no se puede deshacer."
        )

        if not confirmacion:
            return

        try:
            self._servicio.eliminar_por_cedula(str(cedula))
            self._actualizar_tabla()
            self._accion_limpiar()
            self._actualizar_estado(
                f"✔  Visitante '{nombre}' eliminado del registro.",
                color="#FCA5A5"
            )
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _accion_limpiar(self) -> None:
        """Limpia todos los campos del formulario y restaura los placeholders."""
        placeholders = {
            self._var_cedula:  "Ej: 1104567890",
            self._var_nombre:  "Ej: María García",
            self._var_motivo:  "Ej: Reunión de trabajo",
        }
        for variable, placeholder in placeholders.items():
            variable.set(placeholder)

        # Deseleccionar tabla
        for item in self._tabla.selection():
            self._tabla.selection_remove(item)

        self._root.focus()
        self._actualizar_estado(
            "↺  Campos limpiados. Listo para nuevo registro.",
            color="#94A3B8"
        )

    # ──────────────────────────────────────────
    # Métodos auxiliares de la UI
    # ──────────────────────────────────────────

    def _leer_campo(self, variable: tk.StringVar) -> str:
        """
        Lee el valor de un campo ignorando el texto de placeholder.

        Args:
            variable (tk.StringVar): Variable del campo.

        Returns:
            str: Valor real del campo (vacío si era placeholder).
        """
        placeholders = {
            "Ej: 1104567890",
            "Ej: María García",
            "Ej: Reunión de trabajo",
        }
        valor = variable.get().strip()
        return "" if valor in placeholders else valor

    def _actualizar_tabla(self) -> None:
        """Recarga el Treeview con los datos actuales del servicio."""
        # Limpiar filas existentes
        for fila in self._tabla.get_children():
            self._tabla.delete(fila)

        visitantes = self._servicio.obtener_todos()

        for indice, visitante in enumerate(visitantes, start=1):
            etiqueta = "par" if indice % 2 == 0 else "impar"
            self._tabla.insert(
                "",
                tk.END,
                values=(indice, visitante.cedula, visitante.nombre, visitante.motivo),
                tags=(etiqueta,)
            )

        total = self._servicio.total_visitantes()
        texto = f"{total} registro{'s' if total != 1 else ''}"
        self._lbl_contador.configure(text=texto)

    def _actualizar_estado(self, mensaje: str, color: str = "#94A3B8") -> None:
        """
        Actualiza el texto de la barra de estado.

        Args:
            mensaje (str): Mensaje a mostrar.
            color   (str): Color del texto.
        """
        self._lbl_estado.configure(text=mensaje, fg=color)

    # ──────────────────────────────────────────
    # Ejecución de la aplicación
    # ──────────────────────────────────────────

    def iniciar(self) -> None:
        """Lanza el loop principal de la aplicación Tkinter."""
        self._root.mainloop()