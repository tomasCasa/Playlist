import sqlite3
from sqlite3 import Error


def conectar_base():
    try:
        con = sqlite3.connect('mibase.db')
        return con
    except Error:
        print(Error)


def crear_tabla(conec):
    cursor_obj = conec.cursor()
    tabla = "CREATE TABLE IF NOT EXISTS playlist(id integer PRIMARY KEY AUTOINCREMENT, " \
            "nombre text, duracion text, fecha text)"
    cursor_obj.execute(tabla)
    conec.commit()


def insertar_cancion(conec, nombre, duracion):
    cursor_obj = conec.cursor()
    insert = "INSERT INTO playlist(nombre,duracion,fecha) VALUES('%s', '%s',datetime('now'))" \
             % (nombre, duracion)
    cursor_obj.execute(insert)
    conec.commit()


def cerrar_conecion(conec):
    conec.close()


def borrar_cancion(conec, identificador):
    cursor_obj = conec.cursor()
    cursor_obj.execute("DELETE from playlist where id = '%s'" % identificador)
    conec.commit()


def consultar_cancion(conec, identificador):
    sql = 'SELECT id, nombre, duracion, date(fecha) FROM playlist where id = %s' % identificador

    cursor_obj = conec.cursor()
    cursor_obj.execute(sql)
    return cursor_obj.fetchall()


def modificar_cancion(conec, identificador, nombre, duracion):
    cursor_obj = conec.cursor()
    cursor_obj.execute("""UPDATE playlist SET nombre = '%s', duracion = '%s', 
                                                fecha = datetime('now') where id = '%s'"""
                       % (nombre, duracion, identificador))
    conec.commit()


def consulta_all_base(conec):
    sql = 'SELECT id, nombre, duracion, date(fecha) FROM playlist ORDER BY id DESC'

    cursor_obj = conec.cursor()
    cursor_obj.execute(sql)
    return cursor_obj.fetchall()
