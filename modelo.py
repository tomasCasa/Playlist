import validador
import base_peewee
from logger import log_inicio_app
from observador import Observable


class Ejecutable(Observable):
    @log_inicio_app
    def __init__(self):
        print("Ejecutable creado...")
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()

    def get_estado(self):
        return self.estado

    def insertar_cancion(self, nombre, duracion):
        self.set_estado("Se quizo dar de alta una cancion")
        try:
            if len(duracion) == 0:
                validador.error_patron("La duracion no debe estar vacia")
                raise TypeError("La duracion no debe estar vacia")
            if len(nombre) == 0:
                validador.error_patron("El nombre no debe estar vacio")
                raise TypeError("El nombre no debe estar vacio")
            if not validador.validar_duracion(duracion):
                validador.error_patron("El formato de la duracion de la cancion debe ser MM:SS")
                raise TypeError("El formato de la duracion de la cancion debe ser MM:SS")
            if not validador.validar_nombre(nombre):
                validador.error_patron("""El formato del nombre de la cancion debe terminar con .mp3 y 
                                no tener los simbolos '<' y '>'""")
                raise TypeError("""El formato del nombre de la cancion debe terminar con .mp3 y 
                    no tener los simbolos '<' y '>'""")

            base_peewee.insertar_cancion(nombre, duracion)
            validador.info_validacion("Se inserto el dato correctamente")

        except TypeError as mensaje:
            print("Ocurrió una excepción identificada.", mensaje)

    def borrar_cancion(self, identificador):
        self.set_estado("Se quizo borrar una cancion")
        try:
            if len(identificador) == 0:
                validador.error_patron("El id no puede tener ese formato sin nada")
                raise TypeError("El id no puede tener ese formato sin nada")
            if not validador.validar_id(identificador):
                validador.error_patron("El id no puede tener ese formato")
                raise TypeError("El id no puede tener ese formato")

            resultado = base_peewee.consultar_cancion(identificador)

            if not len(resultado) != 0:
                validador.error_borrar("El id que quiere borrar no existe")
                raise TypeError("El id que quiere borrar no existe")

            base_peewee.borrar_cancion(identificador)
            validador.info_validacion("Se elimino el dato correctamente")

        except TypeError as mensaje:
            print("Ocurrió una excepción identificada.", mensaje)

    def modificar_cancion(self, identificador, nombre, duracion):
        self.set_estado("Se quizo de modificar una cancion")
        try:
            if len(identificador) == 0:
                validador.error_patron("El id no puede tener ese formato sin nada")
                raise TypeError("El id no puede tener ese formato sin nada")
            if len(duracion) == 0:
                validador.error_patron("La duracion no debe estar vacia")
                raise TypeError("La duracion no debe estar vacia")
            if len(nombre) == 0:
                validador.error_patron("El nombre no debe estar vacio")
                raise TypeError("El nombre no debe estar vacio")
            if not validador.validar_id(identificador):
                validador.error_patron("El id no puede tener ese formato")
                raise TypeError("El id no puede tener ese formato")
            if not validador.validar_duracion(duracion):
                validador.error_patron("El formato de la duracion de la cancion debe ser MM:SS")
                raise TypeError("El formato de la duracion de la cancion debe ser MM:SS")
            if not validador.validar_nombre(nombre):
                validador.error_patron("""El formato del nombre de la cancion debe terminar con .mp3 y 
                    no tener los simbolos '<' y '>'""")
                raise TypeError("""El formato del nombre de la cancion debe terminar con .mp3 y 
                    no tener los simbolos '<' y '>'""")

            resultado = base_peewee.consultar_cancion(identificador)

            if len(resultado) == 0:
                validador.error_borrar("El id que quiere modificar no existe")
                raise TypeError("El id que quiere modificar no existe")

            base_peewee.modificar_cancion(identificador, nombre, duracion)
            validador.info_validacion("Se modifico el dato correctamente")

        except TypeError as mensaje:
            print("Ocurrió una excepción identificada.", mensaje)

    def traer_base(self):
        self.set_estado("Se quizo consultar una cancion")
        return base_peewee.consulta_all_base()
