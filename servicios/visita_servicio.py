"""
Módulo: servicios/visita_servicio.py
Descripción: Contiene la lógica de negocio (CRUD) del sistema.
             Gestiona la colección de visitantes de forma encapsulada.
             No tiene conocimiento de la interfaz gráfica.
"""

from modelos.visitante import Visitante


class VisitaServicio:
    """
    Servicio que encapsula toda la lógica de negocio para la gestión de visitantes.

    Principios aplicados:
        - Encapsulamiento: la lista interna no es accesible directamente desde fuera.
        - Responsabilidad única: solo gestiona operaciones CRUD sobre visitantes.
        - Sin dependencias externas: opera únicamente sobre objetos del modelo.
    """

    def __init__(self) -> None:
        """
        Constructor del servicio.
        Inicializa la estructura interna de almacenamiento en memoria.
        """
        self._visitantes: list[Visitante] = []

    # ──────────────────────────────────────────
    # Operaciones CRUD
    # ──────────────────────────────────────────

    def registrar(self, cedula: str, nombre: str, motivo: str) -> Visitante:
        """
        Crea y registra un nuevo visitante en el sistema.

        Args:
            cedula (str): Cédula única del visitante.
            nombre (str): Nombre completo del visitante.
            motivo (str): Motivo de la visita.

        Returns:
            Visitante: El objeto visitante recién registrado.

        Raises:
            ValueError: Si algún campo está vacío o la cédula ya existe.
        """
        self._validar_campos(cedula, nombre, motivo)
        self._validar_cedula_unica(cedula)

        nuevo_visitante = Visitante(cedula, nombre, motivo)
        self._visitantes.append(nuevo_visitante)
        return nuevo_visitante

    def obtener_todos(self) -> list[Visitante]:
        """
        Retorna una copia de la lista de todos los visitantes registrados.

        Returns:
            list[Visitante]: Lista de visitantes (copia defensiva).
        """
        return list(self._visitantes)

    def eliminar_por_cedula(self, cedula: str) -> Visitante:
        """
        Elimina un visitante del sistema a partir de su cédula.

        Args:
            cedula (str): Cédula del visitante a eliminar.

        Returns:
            Visitante: El objeto visitante que fue eliminado.

        Raises:
            ValueError: Si no se encuentra ningún visitante con esa cédula.
        """
        visitante = self._buscar_por_cedula(cedula)
        self._visitantes.remove(visitante)
        return visitante

    def buscar_por_cedula(self, cedula: str) -> Visitante | None:
        """
        Busca y retorna un visitante por su cédula (interfaz pública).

        Args:
            cedula (str): Cédula a buscar.

        Returns:
            Visitante | None: El visitante encontrado o None si no existe.
        """
        for visitante in self._visitantes:
            if visitante.cedula == cedula.strip():
                return visitante
        return None

    def total_visitantes(self) -> int:
        """
        Retorna el número total de visitantes registrados.

        Returns:
            int: Cantidad de visitantes en el sistema.
        """
        return len(self._visitantes)

    # ──────────────────────────────────────────
    # Métodos privados de validación
    # ──────────────────────────────────────────

    def _validar_campos(self, cedula: str, nombre: str, motivo: str) -> None:
        """
        Valida que ningún campo esté vacío.

        Args:
            cedula (str): Cédula a validar.
            nombre (str): Nombre a validar.
            motivo (str): Motivo a validar.

        Raises:
            ValueError: Si algún campo está vacío o contiene solo espacios.
        """
        if not cedula or not cedula.strip():
            raise ValueError("La cédula no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not motivo or not motivo.strip():
            raise ValueError("El motivo de la visita no puede estar vacío.")

    def _validar_cedula_unica(self, cedula: str) -> None:
        """
        Verifica que la cédula no esté ya registrada.

        Args:
            cedula (str): Cédula a verificar.

        Raises:
            ValueError: Si ya existe un visitante con esa cédula.
        """
        if self.buscar_por_cedula(cedula) is not None:
            raise ValueError(f"Ya existe un visitante registrado con la cédula '{cedula}'.")

    def _buscar_por_cedula(self, cedula: str) -> Visitante:
        """
        Búsqueda interna que lanza excepción si no encuentra al visitante.

        Args:
            cedula (str): Cédula a buscar.

        Returns:
            Visitante: El visitante encontrado.

        Raises:
            ValueError: Si no se encuentra ningún visitante con esa cédula.
        """
        visitante = self.buscar_por_cedula(cedula)
        if visitante is None:
            raise ValueError(f"No se encontró ningún visitante con la cédula '{cedula}'.")
        return visitante