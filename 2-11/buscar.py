import subprocess
import tkinter as tk
from base_datos.receta import Receta


base_datos="base_datos/recetas.db"
receta=Receta(base_datos)
base_datos=Receta(base_datos)
def volver():
        root.destroy()
        subprocess.run(['python', "recetas.py"])
class Buscar:

    def __init__(self, root):
        self.root = root
        self.root.title("Buscar Receta")
        self.busqueda()
        self.root.geometry("500x400")
        self.root.config(background="yellow")

    def busqueda (self):
        tk.Button(self.root, text="Buscar", foreground="white", background="black", command=self.receta_buscada).pack()
        boton_link=tk.Button(root, text="Atras", command=volver)
        boton_link.pack()

    def receta_buscada(self):
        recetas=receta.mostrar_recetas()
        if recetas:
            for fila in recetas:
                boton=tk.Label(root, text=(fila))
                boton.pack()

if __name__ == "__main__":
    root = tk.Tk()
    buscar = Buscar(root)
    root.mainloop()     