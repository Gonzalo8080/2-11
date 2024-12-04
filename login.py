import subprocess
import tkinter as tk
from tkinter import messagebox
from base_datos.usuario import Usuario


base_datos="base_datos/usuarios.db"
usuario=Usuario(base_datos)
base_datos=Usuario(base_datos)
def volver():
        root.destroy()
        subprocess.run(['python', "main.py"])

def ir():
    root.destroy()
    subprocess.run(['python', "recetas.py"])

class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Iniciar sesion")
        self.iniciar_sesion()
        self.root.geometry("500x400")
        self.root.config(background="grey")

    def iniciar_sesion(self):
        tk.Label(self.root, text="Nombre de Usuario", foreground="white", background="black").pack()
        
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()
        tk.Label(self.root, text="Contraseña", foreground="white", background="black").pack()
        self.contraseña_entry = tk.Entry(self.root, show="*")
        self.contraseña_entry.pack()
        tk.Button(self.root, text="Iniciar Sesion", foreground="white", background="black", command=self.sesion).pack()
        boton_link=tk.Button(root, text="Atras", command=volver)
        boton_link.pack()

    def sesion(self):
            nombre = self.nombre_entry.get()
            contraseña = self.contraseña_entry.get()

            if nombre and contraseña:
                try:
                    messagebox.showinfo("Registro", "Bienvenido " + nombre)
                    boton_link=tk.Button(root, text="Ir a recetas", command=ir)
                    boton_link.pack()
                    
                except Exception:
                    messagebox.showerror("Error", "Nombre o Contraseña incorrecta")
            else:
                messagebox.showerror("Error", "Ingrese todos los datos")

if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root)
    root.mainloop()     
