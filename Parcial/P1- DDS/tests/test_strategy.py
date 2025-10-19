import unittest
from unittest.mock import MagicMock
import sys
import os

# Adds the 'src' directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now the imports will work correctly
from servicios.personal.contratista import Contratista
from servicios.negocio.estrategias_cosecha import CosechaManual, CosechaMecanica
from servicios.creacion.finca_builder import FincaBuilder

class TestCosechaStrategy(unittest.TestCase):
    def setUp(self):
        self.contratista = Contratista("Gómez")
        self.finca = FincaBuilder(20).build()
        self.finca.cosechar = MagicMock()

    def test_estrategia_manual_ejecuta_la_cosecha(self):
        self.contratista.set_estrategia(CosechaManual())
        self.contratista.ejecutar_cosecha(self.finca)
        self.finca.cosechar.assert_called_once()

    def test_estrategia_mecanica_ejecuta_la_cosecha(self):
        self.contratista.set_estrategia(CosechaMecanica())
        self.contratista.ejecutar_cosecha(self.finca)
        self.finca.cosechar.assert_called_once()

if __name__ == '__main__':
    unittest.main()