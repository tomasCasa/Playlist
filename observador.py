import datetime


class Observable:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        for observador in self.observadores:
            observador.update()


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ObservadorConcreto(Observador):
    def __init__(self, obj):
        self.observado = obj
        self.observado.agregar(self)

    def update(self):
        self.estado = self.observado.get_estado()
        with open("infoApp.log", 'a', encoding='utf-8') as f:
            f.write("[" + str(datetime.datetime.now()) + "]: "+self.estado+"\n")
            f.close()
