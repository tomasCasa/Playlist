import base_de_datos
from base_de_datos import conectar_base
from base_de_datos import crear_tabla
import validador


def insertar_cancion(conec, nombre, duracion):
    if validador.validar_duracion(duracion):
        if validador.validar_nombre(nombre):
            base_de_datos.insertar_cancion(conec, nombre, duracion)
            validador.info_validacion("Se inserto el dato correctamente")
        else:
            validador.error_patron("""El formato del nombre de la cancion debe terminar con .mp3 
                          y no tener los simbolos '<' y '>'""")
    else:
        validador.error_patron("El formato de la duracion de la cancion debe ser MM:SS")


def borrar_cancion(conec, identificador):
    if validador.validar_id(identificador):
        if len(identificador) != 0:
            resultado = base_de_datos.consultar_cancion(conec, identificador)
            if len(resultado) != 0:
                base_de_datos.borrar_cancion(conec, identificador)
                validador.info_validacion("Se elimino el dato correctamente")
            else:
                validador.error_borrar("El id que quiere borrar no existe")
        else:
            validador.error_patron("El id no puede tener ese formato sin nada")
    else:
        validador.error_patron("El id no puede tener ese formato")


def modificar_cancion(conec, identificador, nombre, duracion):
    if validador.validar_id(identificador):
        if len(identificador) != 0:
            if validador.validar_duracion(duracion):
                if validador.validar_nombre(nombre):
                    resultado = base_de_datos.consultar_cancion(conec, identificador)
                    if len(resultado) != 0:
                        base_de_datos.modificar_cancion(conec, identificador, nombre, duracion)
                        validador.info_validacion("Se modifico el dato correctamente")
                    else:
                        validador.error_borrar("El id que quiere modificar no existe")
                else:
                    validador.error_patron("""El formato del nombre de la cancion debe terminar con .mp3 
                                  y no tener los simbolos '<' y '>'""")
            else:
                validador.error_patron("El formato de la duracion de la cancion debe ser MM:SS")
        else:
            validador.error_patron("El id no puede tener ese formato sin nada")
    else:
        validador.error_patron("El id no puede tener ese formato")


def mostrar(conec, tree):
    # limpieza de tabla
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    resultado = base_de_datos.consulta_all_base(conec)

    for fila in resultado:
        tree.insert('', 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


def cerrar_programa(conec, root):
    base_de_datos.cerrar_conecion(conec)
    root.quit()
