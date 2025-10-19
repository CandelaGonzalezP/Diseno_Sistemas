import unittest
import sys
import os

# Adds the 'src' directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now the imports will work correctly
from servicios.creacion.finca_builder import FincaBuilder
from entidades.terrenos.finca import Finca

class TestFincaBuilder(unittest.TestCase):
    def test_construye_finca_con_valores_personalizados(self):
        finca = (FincaBuilder(hectareas=50)
                   .con_nombre("Finca Test")
                   .con_tipo_suelo("Arenoso")
                   .build())
        self.assertIsInstance(finca, Finca)
        self.assertEqual(finca.hectareas, 50)
        self.assertEqual(finca.nombre, "Finca Test")
        self.assertEqual(finca.tipo_suelo, "Arenoso")

    def test_construye_finca_con_valores_por_defecto(self):
        finca = FincaBuilder(hectareas=100).build()
        self.assertEqual(finca.nombre, "Finca Sin Nombre")
        self.assertEqual(finca.tipo_suelo, "Franco Arcilloso")

if __name__ == '__main__':
    unittest.main()