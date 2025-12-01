"""
Punto de entrada del Simulador de Sistema Operativo
Inicia la interfaz gráfica del simulador
"""

import tkinter as tk
from interfaz import SimuladorApp


def main():
    """Función principal que inicia la aplicación"""
    root = tk.Tk()
    app = SimuladorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
