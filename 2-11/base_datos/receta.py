import sqlite3

class Receta:
    def __init__(self, nombre_bd):
        self.nombre_bd=nombre_bd
        self.receta=sqlite3.connect(nombre_bd)
        self.cursor=self.receta.cursor()

    def crear_tabla_receta(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS recetas(nombre TEXT, ingredientes TEXT, categoria TEXT)")
        self.receta.commit()

    def insertar_receta(self,nombre, ingredientes, categoria):
        self.cursor.execute("INSERT INTO recetas VALUES(?,?,?)",(nombre, ingredientes, categoria))
        self.receta.commit()

    def mostrar_recetas(self):
        self.cursor.execute("SELECT * FROM recetas")
        recetas=self.cursor.fetchall()
        return recetas
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.receta.close()