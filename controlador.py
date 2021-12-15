from tkinter import *
from vista import Ventana
"""import base_de_datos
from base_de_datos import Coneccion
import validador"""


class Controlador:
    def __init__(self, root):
        self.root_controller = root
        self.ventanta = Ventana(root)


if __name__ == "__main__":
    root = Tk()
    app = Controlador(root)
    root.mainloop()
