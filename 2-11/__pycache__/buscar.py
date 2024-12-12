import subprocess
import tkinter as tk
from tkinter import messagebox
from base_datos.receta import Receta

base_datos = "base_datos/recetas.db"
receta = Receta(base_datos)

def volver():
    root.destroy()
    subprocess.run(['python', "recetas.py"])

class Buscar:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscar Receta")
        self.busqueda()
        self.root.geometry("500x400")
        self.root.config(background="grey")

    def busqueda(self):
        tk.Button(self.root, text="Buscar", foreground="white", background="black", command=self.receta_buscada).pack()
        boton_link = tk.Button(self.root, text="Atras", command=volver)
        boton_link.pack()

    def receta_buscada(self):
        recetas = receta.mostrar_recetas()
        if recetas:
            for fila in recetas:
                
                receta_nombre, receta_descripcion = fila[0], fila[1]
                receta_info = f"{receta_nombre}: {receta_descripcion}"
                
                
                receta_frame = tk.Frame(self.root, bg="white", padx=10, pady=5)
                receta_frame.pack(fill="x", pady=2)
                
                
                tk.Label(receta_frame, text=receta_info, bg="white", anchor="w").pack(side="left", fill="x", expand=True)
                
                
                tk.Button(receta_frame, text="Eliminar", bg="red", fg="white", command=lambda nombre=receta_nombre: self.eliminar_receta(nombre)).pack(side="right")

    def eliminar_receta(self, receta_nombre):
        
        confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar la receta '{receta_nombre}'?")
        if confirmacion:
            exito = receta.eliminar_receta(receta_nombre)
            if exito:
                messagebox.showinfo("Éxito", "La receta fue eliminada exitosamente.")
                self.receta_buscada()  
            else:
                messagebox.showerror("Error", "Hubo un problema al eliminar la receta.")

if __name__ == "__main__":
    root = tk.Tk()
    buscar = Buscar(root)
    root.mainloop()

