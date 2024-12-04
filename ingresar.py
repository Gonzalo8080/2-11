import subprocess
import tkinter as tk
from tkinter import messagebox
from base_datos.receta import Receta


base_datos="base_datos/recetas.db"
receta=Receta(base_datos)
base_datos=Receta(base_datos)
receta.crear_tabla_receta()
def volver():
        root.destroy()
        subprocess.run(['python', "recetas.py"])
class Ingresar:

    def __init__(self, root):
        self.root = root
        self.root.title("Agregar Receta")
        self.ingreso()
        self.root.geometry("500x400")
        self.root.config(background="grey")

    def ingreso (self):
        tk.Label(self.root, text="Nombre de la Receta", foreground="white", background="black").pack()
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()
        tk.Label(self.root, text="Ingredientes (separados con ,)", foreground="white", background="black").pack()
        self.ingredientes_entry = tk.Entry(self.root)
        self.ingredientes_entry.pack()
        tk.Label(self.root, text="Categoria (salado o dulce)", foreground="white", background="black").pack()
        self.categoria_entry = tk.Entry(self.root)
        self.categoria_entry.pack()
        tk.Button(self.root, text="Ingresar", foreground="white", background="black", command=self.receta_ingresada).pack()
        boton_link=tk.Button(root, text="Atras", command=volver)
        boton_link.pack()

    def receta_ingresada(self):
        nombre = self.nombre_entry.get()
        ingredientes = self.ingredientes_entry.get()
        categoria = self.categoria_entry.get()
        
        if nombre and ingredientes and categoria:
            try:
                receta.insertar_receta(nombre, ingredientes, categoria)
                messagebox.showinfo("Registro", "receta ingresada exitosamente")
            except Exception:
                messagebox.showerror("Error", "Receta ya existe")
        else:
            messagebox.showerror("Error", "Por favor, ingrese todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    ingresar = Ingresar(root)
    root.mainloop()     