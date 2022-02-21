from tkinter import *
from vista import Ventana


class Controlador:
    def __init__(self, root):
        self.root_controller = root
        self.ventanta = Ventana(root)


if __name__ == "__main__":
    root = Tk()
    app = Controlador(root)
    root.mainloop()
