import subprocess
import tkinter as tk
from tkinter import messagebox
from base_datos.usuario import Usuario


base_datos="base_datos/usuarios.db"
usuario=Usuario(base_datos)
base_datos=Usuario(base_datos)
usuario.crear_tabla_usuario()
def volver():
        root.destroy()
        subprocess.run(['python', "main.py"])
class Registrar:

    def __init__(self, root):
        self.root = root
        self.root.title("Agregar Usuario")
        self.registro()
        self.root.geometry("500x400")
        self.root.config(background="red")

    def registro (self):
        tk.Label(self.root, text="Nombre de Usuario", foreground="white", background="black").pack()
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()
        tk.Label(self.root, text="Contraseña", foreground="white", background="black").pack()
        self.contraseña_entry = tk.Entry(self.root, show="*")
        self.contraseña_entry.pack()
        tk.Button(self.root, text="Registrarse", foreground="white", background="black", command=self.registrarse).pack()
        boton_link=tk.Button(root, text="Atras", command=volver)
        boton_link.pack()

    def registrarse(self):
        nombre = self.nombre_entry.get()
        contraseña = self.contraseña_entry.get()
        
        if nombre and contraseña:
            try:
                usuario.insertar_usuario(nombre, contraseña)
                messagebox.showinfo("Registro", "Usuario registrado exitosamente")
            except Exception:
                messagebox.showerror("Error", "Nombre de usuario ya existe")
        else:
            messagebox.showerror("Error", "Por favor, ingrese todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    registrar = Registrar(root)
    root.mainloop()     



