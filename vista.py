from tkinter import *
from tkinter import ttk
from modelo import Ejecutable


class Ventana:
    def __init__(self, root):
        self.root_vista = root
        self.ejecutador = Ejecutable()
        # Defino las variables que voy a usar
        self.nombre = StringVar()
        self.duracion = StringVar()
        self.identificador = StringVar()

        # Fijo el tamaño de la ventana y el título
        self.root_vista.resizable(width=False, height=False)
        self.root_vista.title("Base de datos de Playlist")

        # Creo las etiquetas y los botones
        self.l_nombre = ttk.Label(self.root_vista, text="Nombre")
        self.l_duracion = ttk.Label(self.root_vista, text="Duracion")
        self.l_identificador = ttk.Label(self.root_vista, text="Id")
        self.l_espacio = ttk.Label(self.root_vista, text="")

        self.e_nombre = ttk.Entry(self.root_vista, textvariable=self.nombre, width=15)
        self.e_duracion = ttk.Entry(self.root_vista, textvariable=self.duracion, width=15)
        self.e_identificador = ttk.Entry(self.root_vista, textvariable=self.identificador, width=15)
        self.tree = ttk.Treeview(self.root_vista)

        self.b_agregar = ttk.Button(self.root_vista,
                                    text="Agregar",
                                    command=lambda: self.insertar_cancion(self.e_nombre.get(),
                                                                          self.e_duracion.get()))
        self.b_borrar = ttk.Button(self.root_vista,
                                   text="Borrar",
                                   command=lambda: self.borrar_cancion(self.e_identificador.get()))
        self.b_modificar = ttk.Button(self.root_vista,
                                      text="Modificar",
                                      command=lambda: self.modificar_cancion(self.e_identificador.get(),
                                                                             self.e_nombre.get(),
                                                                             self.e_duracion.get()))
        self.b_mostrar = ttk.Button(self.root_vista,
                                    text="Mostrar DB",
                                    command=lambda: self.mostrar(self.tree))
        self.b_salir = ttk.Button(self.root_vista,
                                  text="Salir",
                                  command=lambda: self.cerrar_programa())

        # Armo la tabla para mostrar los datos de la DB
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Duracion")
        self.tree.heading("col3", text="Fecha")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=80, minwidth=80)
        self.tree.column("col2", width=80, minwidth=80)
        self.tree.column("col3", width=100, minwidth=100)
        self.tree.column("col4", width=100, minwidth=100)

        # Posiciono los controles
        self.l_nombre.grid(column=0, row=0)
        self.l_duracion.grid(column=0, row=1)
        self.l_identificador.grid(column=2, row=0)
        self.e_nombre.grid(column=1, row=0)
        self.e_duracion.grid(column=1, row=1)
        self.e_identificador.grid(column=3, row=0)
        self.tree.grid(column=0, row=5, columnspan=4)
        self.b_agregar.grid(column=0, row=4)
        self.b_borrar.grid(column=2, row=4)
        self.b_modificar.grid(column=1, row=4)
        self.b_mostrar.grid(column=3, row=4)
        self.l_espacio.grid(column=0, row=3)
        self.b_salir.grid(column=3, row=6)

    def insertar_cancion(self, nombre, duracion):
        self.ejecutador.insertar_cancion(nombre, duracion)

    def borrar_cancion(self, identificador):
        self.ejecutador.borrar_cancion(identificador)

    def modificar_cancion(self, identificador, nombre, duracion):
        self.ejecutador.modificar_cancion(identificador, nombre, duracion)

    def mostrar(self, tree):
        # limpieza de tabla
        records = tree.get_children()
        for element in records:
            tree.delete(element)

        resultado = self.ejecutador.traer_base()

        # llenado de tabla
        for fila in resultado:
            tree.insert('', 0, text=fila.id, values=(fila.nombre, fila.duracion, fila.fecha))

    def cerrar_programa(self, ):
        self.root_vista.quit()
