from sqlite3 import Error
from peewee import *
from logger import *
import datetime

try:
    db = SqliteDatabase('PlaylistPeewee.db')

    class BaseModel(Model):
        class Meta:
            database = db

    class CancionDB(BaseModel):
        nombre = TextField()
        duracion = TextField()
        fecha = DateTimeField(default=datetime.datetime.now)

    db.connect()
    db.create_tables([CancionDB])

except Error:
    print(Error)


@log_alta
def insertar_cancion(nombre, duracion):
    cancion_db = CancionDB()
    cancion_db.nombre = nombre
    cancion_db.duracion = duracion
    cancion_db.save()


@log_borrar
def borrar_cancion(identificador):
    borrar = CancionDB.get(CancionDB.id == identificador)
    borrar.delete_instance()


@log_consultar
def consultar_cancion(identificador):
    return CancionDB.select().where(CancionDB.id == identificador)


@log_modificacion
def modificar_cancion(identificador, nombre_param, duracion_param):
    actualizar = CancionDB.update(nombre=nombre_param, duracion=duracion_param).where(CancionDB.id == identificador)
    actualizar.execute()


@log_consultar
def consulta_all_base():
    return CancionDB.select()
