import sqlite3

class Usuario:
    def __init__(self, nombre_bd):
        self.nombre_bd=nombre_bd
        self.usuario=sqlite3.connect(nombre_bd)
        self.cursor=self.usuario.cursor()

    def crear_tabla_usuario(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios( nombre TEXT, contraseña TEXT)")
        self.usuario.commit()

    def insertar_usuario(self, nombre, contraseña):
        self.cursor.execute("INSERT INTO usuarios VALUES(?,?)",(nombre,contraseña))
        self.usuario.commit()

    def seleccionar_usuario(self, nombre, contraseña):
        self.cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ?", (nombre, contraseña))
        self.usuario.commit()
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.usuario.close()
    
    def eliminar_usuario(self,nombre):
        self.cursor.execute("DELETE FROM usuarios WHERE nombre=?",(nombre,))  
        self.usuario.commit()

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT *FROM usuarios")
        usuarios=self.cursor.fetchall()
        return usuarios