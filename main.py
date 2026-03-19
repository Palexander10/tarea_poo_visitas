"""
main.py — Punto de entrada del Sistema de Registro de Visitantes.

Responsabilidad:
    Instancia las capas en el orden correcto (Servicio → UI) y
    arranca la aplicación.  No contiene lógica de negocio ni código de UI.

Ejecución:
    python main.py
"""

from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter


def main() -> None:
    """
    Función principal de arranque.

    Flujo:
        1. Crea el servicio (capa de negocio).
        2. Inyecta el servicio en la interfaz gráfica.
        3. Inicia el bucle principal de la aplicación.
    """
    servicio = VisitaServicio()          # Capa de Servicios
    app = AppTkinter(servicio)           # Capa UI — recibe servicio por inyección
    app.iniciar()                        # Arranca el loop de Tkinter


if __name__ == "__main__":
    main()