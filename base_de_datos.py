import sqlite3
from sqlite3 import Error


class Coneccion:
    def __init__(self,):
        try:
            conec = self.conexion()
            cursor_obj = conec.cursor()
            tabla = "CREATE TABLE IF NOT EXISTS playlist(id integer PRIMARY KEY AUTOINCREMENT, " \
                    "nombre text, duracion text, fecha text)"
            cursor_obj.execute(tabla)
            conec.commit()
            self.cerrar_conecion(conec)
        except Error:
            print(Error)

    def conexion(self,):
        conec = sqlite3.connect('mibase.db')
        return conec

    def insertar_cancion(self,
                         nombre,
                         duracion):
        conec = self.conexion()
        cursor_obj = conec.cursor()
        insert = "INSERT INTO playlist(nombre,duracion,fecha) VALUES('%s', '%s',datetime('now'))" \
                 % (nombre, duracion)
        cursor_obj.execute(insert)
        conec.commit()
        self.cerrar_conecion(conec)

    def cerrar_conecion(self, conec):
        conec.close()

    def borrar_cancion(self, identificador):
        conec = self.conexion()
        cursor_obj = conec.cursor()
        cursor_obj.execute("DELETE from playlist where id = '%s'" % identificador)
        conec.commit()
        self.cerrar_conecion(conec)

    def consultar_cancion(self, identificador):
        conec = self.conexion()
        sql = 'SELECT id, nombre, duracion, date(fecha) FROM playlist where id = %s' % identificador

        cursor_obj = conec.cursor()
        cursor_obj.execute(sql)
        resultados = cursor_obj.fetchall()
        self.cerrar_conecion(conec)
        return resultados

    def modificar_cancion(self, identificador, nombre, duracion):
        conec = self.conexion()
        cursor_obj = conec.cursor()
        cursor_obj.execute("""UPDATE playlist SET nombre = '%s', duracion = '%s', 
                                                    fecha = datetime('now') where id = '%s'"""
                           % (nombre, duracion, identificador))
        conec.commit()
        self.cerrar_conecion(conec)

    def consulta_all_base(self,):
        conec = self.conexion()
        sql = 'SELECT id, nombre, duracion, date(fecha) FROM playlist ORDER BY id DESC'

        cursor_obj = conec.cursor()
        cursor_obj.execute(sql)
        resultados = cursor_obj.fetchall()
        self.cerrar_conecion(conec)
        return resultados
