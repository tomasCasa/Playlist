import re
from tkinter.messagebox import *

patron_duracion = "^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]){2}$"
patron_nombre_cancion = "^[^<,>]*(\.mp3)$"
patron_id = "^[0-9]+$"


def error_patron(mensaje):
    showerror("Error de Patron", "%s" % mensaje)


def error_borrar(mensaje):
    showerror("Error de Eliminacion", "%s" % mensaje)


def info_validacion(mensaje):
    showinfo(title="Valido", message=mensaje)


def validar_duracion(duracion):
    return re.match(patron_duracion, duracion)


def validar_nombre(nombre):
    return re.match(patron_nombre_cancion, nombre)


def validar_id(identificador):
    return re.match(patron_id, identificador)
