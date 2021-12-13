from tkinter import *
from vista import Ventana
"""import base_de_datos
from base_de_datos import Coneccion
import validador"""


class Controlador:
    def __init__(self, root):
        self.root_controller = root
        #self.conection = Coneccion()
        self.ventanta = Ventana(root)

    """def insertar_cancion(self, nombre, duracion):
        if validador.validar_duracion(duracion):
            if validador.validar_nombre(nombre):
                self.conection.insertar_cancion(nombre, duracion)
                validador.info_validacion("Se inserto el dato correctamente")
            else:
                validador.error_patron(""""""El formato del nombre de la cancion debe terminar con .mp3 
                              y no tener los simbolos '<' y '>'"""""")
        else:
            validador.error_patron("El formato de la duracion de la cancion debe ser MM:SS")

    def borrar_cancion(self, identificador):
        if validador.validar_id(identificador):
            if len(identificador) != 0:
                resultado = self.conection.consultar_cancion(identificador)
                if len(resultado) != 0:
                    self.conection.borrar_cancion(identificador)
                    validador.info_validacion("Se elimino el dato correctamente")
                else:
                    validador.error_borrar("El id que quiere borrar no existe")
            else:
                validador.error_patron("El id no puede tener ese formato sin nada")
        else:
            validador.error_patron("El id no puede tener ese formato")

    def modificar_cancion(self, identificador, nombre, duracion):
        if validador.validar_id(identificador):
            if len(identificador) != 0:
                if validador.validar_duracion(duracion):
                    if validador.validar_nombre(nombre):
                        resultado = self.conection.consultar_cancion(identificador)
                        if len(resultado) != 0:
                            self.conection.modificar_cancion(identificador, nombre, duracion)
                            validador.info_validacion("Se modifico el dato correctamente")
                        else:
                            validador.error_borrar("El id que quiere modificar no existe")
                    else:
                        validador.error_patron(""""""El formato del nombre de la cancion debe terminar con .mp3 
                                      y no tener los simbolos '<' y '>'"""""")
                else:
                    validador.error_patron("El formato de la duracion de la cancion debe ser MM:SS")
            else:
                validador.error_patron("El id no puede tener ese formato sin nada")
        else:
            validador.error_patron("El id no puede tener ese formato")

    def mostrar(self, tree):
        # limpieza de tabla
        records = tree.get_children()
        for element in records:
            tree.delete(element)

        resultado = self.conection.consulta_all_base()

        for fila in resultado:
            tree.insert('', 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

    def cerrar_programa(self,):
        self.root_controller.quit()"""


if __name__ == "__main__":
    root = Tk()
    app = Controlador(root)
    root.mainloop()
