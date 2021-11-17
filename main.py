from tkinter import *
from tkinter import ttk
import controlador

conection = controlador.conectar_base()
controlador.crear_tabla(conection)

# Defino la ventana principal de la aplicación
root = Tk()

# Defino las variables que voy a usar
nombre = StringVar()
duracion = StringVar()
identificador = StringVar()

# Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title("Base de datos de Playlist")

# Creo las etiquetas y los botones
l_nombre = ttk.Label(root, text="Nombre")
l_duracion = ttk.Label(root, text="Duracion")
l_identificador = ttk.Label(root, text="Id")
l_espacio = ttk.Label(root, text="")

e_nombre = ttk.Entry(root, textvariable=nombre, width=15)
e_duracion = ttk.Entry(root, textvariable=duracion, width=15)
e_identificador = ttk.Entry(root, textvariable=identificador, width=15)
tree = ttk.Treeview(root)

b_agregar = ttk.Button(root,
                       text="Agregar",
                       command=lambda: controlador.insertar_cancion(conection,
                                                                    e_nombre.get(),
                                                                    e_duracion.get()))
b_borrar = ttk.Button(root,
                      text="Borrar",
                      command=lambda: controlador.borrar_cancion(conection,
                                                                 e_identificador.get()))
b_modificar = ttk.Button(root,
                         text="Modificar",
                         command=lambda: controlador.modificar_cancion(conection,
                                                                       e_identificador.get(),
                                                                       e_nombre.get(),
                                                                       e_duracion.get()))
b_mostrar = ttk.Button(root,
                       text="Mostrar DB",
                       command=lambda: controlador.mostrar(conection, tree))
b_salir = ttk.Button(root,
                     text="Salir",
                     command=lambda: controlador.cerrar_programa(conection, root))

tree["columns"] = ("col1", "col2", "col3", "col4")
tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Duracion")
tree.heading("col3", text="Fecha")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80)
tree.column("col2", width=80, minwidth=80)
tree.column("col3", width=100, minwidth=100)
tree.column("col4", width=100, minwidth=100)

# Posiciono los controles
l_nombre.grid(column=0, row=0)
l_duracion.grid(column=0, row=1)
l_identificador.grid(column=2, row=0)
e_nombre.grid(column=1, row=0)
e_duracion.grid(column=1, row=1)
e_identificador.grid(column=3, row=0)
tree.grid(column=0, row=5, columnspan=4)
b_agregar.grid(column=0, row=4)
b_borrar.grid(column=2, row=4)
b_modificar.grid(column=1, row=4)
b_mostrar.grid(column=3, row=4)
l_espacio.grid(column=0, row=3)
b_salir.grid(column=3, row=6)

mainloop()
