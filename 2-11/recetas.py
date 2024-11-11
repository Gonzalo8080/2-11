import tkinter as tk
import subprocess
from base_datos.usuario import Usuario
from base_datos.receta import Receta

base_datos="base_datos/usuarios.db"
base_datos="base_datos/recetas.db"
usuario=Usuario(base_datos)
receta=Receta(base_datos)

def login():
    root.destroy()
    subprocess.run(['python', "login.py"])

def registrar():
    root.destroy()
    subprocess.run(['python', "registrar.py"])

def ingresar():
    root.destroy()
    subprocess.run(['python', "ingresar.py"])

def buscar():
    root.destroy()
    subprocess.run(['python', "buscar.py"])

root=tk.Tk()
root.geometry("300x200")
root.title("Parcial II Alsogaray")
root.config(background="gray")


boton_link=tk.Button(root, text="ingresar receta", command=ingresar)
boton_link.config(background="blue")
boton_link.config(foreground="yellow")
boton_link.pack()

boton_link=tk.Button(root, text="buscar receta", command=buscar)
boton_link.config(background="yellow")
boton_link.config(foreground="blue")
boton_link.pack()

root.mainloop()