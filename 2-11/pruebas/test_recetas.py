import unittest
from ingresar import ingreso

class test_recetas(unittest.TestCase):
    def receta_valida(self):
        self.assertTrue(ingreso("nombre", "ingrediente1, ingrediente2", "categoria"))
        self.assertTrue(ingreso("algo dulce", "azucar, miel", "dulce"))
        self.assertTrue(ingreso("algo salado", "sal, aceite", "salado"))