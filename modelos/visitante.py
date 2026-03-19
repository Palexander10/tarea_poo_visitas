"""
Módulo  : modelos/visitante.py
Capa    : Modelo (Data Class)
Autor   : Tarea POO – Arquitectura Modular
Descripción:
    Define la clase ``Visitante`` como entidad central del dominio.
    Aplica encapsulamiento mediante atributos privados con propiedades
    de solo lectura, garantizando inmutabilidad del objeto una vez creado.
"""

from __future__ import annotations


class Visitante:
    """
    Representa a un visitante registrado en la oficina.

    La clase actúa como modelo de datos (Value Object): sus atributos
    son de solo lectura una vez construido el objeto, lo que garantiza
    la integridad del registro.

    Attributes:
        cedula (str): Número de cédula o identificación. Actúa como
                      identificador único dentro del sistema.
        nombre (str): Nombre completo del visitante.
        motivo (str): Razón o propósito de la visita a la oficina.

    Example:
        >>> v = Visitante("1104567890", "Ana Torres", "Reunión de trabajo")
        >>> print(v.nombre)
        Ana Torres
    """

    def __init__(self, cedula: str, nombre: str, motivo: str) -> None:
        """
        Inicializa un nuevo Visitante con sus datos esenciales.

        Los valores se normalizan eliminando espacios en los extremos
        antes de ser almacenados.

        Args:
            cedula (str): Cédula única del visitante (no vacía).
            nombre (str): Nombre completo del visitante (no vacío).
            motivo (str): Motivo de la visita (no vacío).
        """
        # Atributos privados: solo accesibles mediante propiedades
        self._cedula: str = cedula.strip()
        self._nombre: str = nombre.strip()
        self._motivo: str = motivo.strip()

    # ------------------------------------------------------------------ #
    #  Propiedades de solo lectura (getters)                              #
    # ------------------------------------------------------------------ #

    @property
    def cedula(self) -> str:
        """Cédula del visitante (identificador único, inmutable)."""
        return self._cedula

    @property
    def nombre(self) -> str:
        """Nombre completo del visitante (inmutable)."""
        return self._nombre

    @property
    def motivo(self) -> str:
        """Motivo de la visita (inmutable)."""
        return self._motivo

    # ------------------------------------------------------------------ #
    #  Métodos de representación                                          #
    # ------------------------------------------------------------------ #

    def __str__(self) -> str:
        """
        Representación amigable para el usuario final.

        Returns:
            str: Cadena con los datos legibles del visitante.
        """
        return (
            f"Visitante | Cédula: {self._cedula} | "
            f"Nombre: {self._nombre} | Motivo: {self._motivo}"
        )

    def __repr__(self) -> str:
        """
        Representación técnica útil para depuración.

        Returns:
            str: Cadena reproducible para recrear el objeto.
        """
        return (
            f"Visitante(cedula={self._cedula!r}, "
            f"nombre={self._nombre!r}, "
            f"motivo={self._motivo!r})"
        )

    # ------------------------------------------------------------------ #
    #  Comparación e identidad                                            #
    # ------------------------------------------------------------------ #

    def __eq__(self, otro: object) -> bool:
        """
        Compara dos visitantes por su cédula (identificador de negocio).

        Args:
            otro (object): Objeto con el que comparar.

        Returns:
            bool: ``True`` si ambos objetos tienen la misma cédula.
        """
        if not isinstance(otro, Visitante):
            return NotImplemented
        return self._cedula == otro._cedula

    def __hash__(self) -> int:
        """
        Calcula el hash del visitante basado en la cédula.

        Necesario al implementar ``__eq__`` para poder usar instancias
        en conjuntos (set) o como claves de diccionario.

        Returns:
            int: Valor hash de la cédula.
        """
        return hash(self._cedula)