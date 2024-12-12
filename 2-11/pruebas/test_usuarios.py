import unittest
from registrar import registro

class test_usuarios(unittest.TestCase):
    def usuario_valido(self):
        self.assertTrue(registro("nombre", "contraseña"))
        self.assertTrue(registro("Gonzalo", "12345678"))