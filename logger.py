import datetime


def log_alta(funcion):
    def envoltura(*arg, **kargs):
        with open("infoDB.log", 'a', encoding='utf-8') as f:
            f.write("["+str(datetime.datetime.now())+"]: Dando una cancion de Alta "
                                                     "con nombre: "+arg[0]+" y duracion: "+arg[1]+"\n")
            f.close()
        return funcion(*arg, **kargs)

    return envoltura


def log_borrar(funcion):
    def envoltura(*arg, **kargs):
        with open("infoDB.log", 'a', encoding='utf-8') as f:
            f.write("["+str(datetime.datetime.now())+"]: Borrando una cancion con id: "+arg[0]+" \n")
            f.close()
        return funcion(*arg, **kargs)

    return envoltura


def log_modificacion(funcion):
    def envoltura(*arg, **kargs):
        with open("infoDB.log", 'a', encoding='utf-8') as f:
            f.write("["+str(datetime.datetime.now())+"]: Modificando una cancion con id: "
                                                     ""+arg[0]+", nombre: "+arg[1]+" y duracion: "+arg[2]+"\n")
            f.close()
        return funcion(*arg, **kargs)

    return envoltura


def log_consultar(funcion):
    def envoltura(*arg, **kargs):
        with open("infoDB.log", 'a', encoding='utf-8') as f:
            f.write("["+str(datetime.datetime.now())+"]: Consultando las canciones\n")
            f.close()
        return funcion(*arg, **kargs)

    return envoltura


def log_inicio_app(funcion):
    def envoltura(*arg, **kargs):
        with open("infoDB.log", 'a', encoding='utf-8') as f:
            f.write("["+str(datetime.datetime.now())+"]: Se inicio la aplicacion\n")
            f.close()
        return funcion(*arg, **kargs)

    return envoltura


def log_salir_app(funcion):
    def envoltura(*arg, **kargs):
        with open("infoDB.log", 'a', encoding='utf-8') as f:
            f.write("["+str(datetime.datetime.now())+"]: Se cierra la aplicacion\n")
            f.close()
        return funcion(*arg, **kargs)

    return envoltura

