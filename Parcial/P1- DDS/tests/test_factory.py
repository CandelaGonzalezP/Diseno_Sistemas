import unittest
import sys
import os

# Adds the 'src' directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now the imports will work correctly
from servicios.creacion.vid_factory import VidFactory
from entidades.cultivos.vid import Malbec, CabernetSauvignon

class TestVidFactory(unittest.TestCase):
    def setUp(self):
        self.fabrica = VidFactory()

    def test_crea_malbec_correctamente(self):
        vid = self.fabrica.crear_vid("malbec")
        self.assertIsInstance(vid, Malbec)

    def test_crea_cabernet_correctamente(self):
        vid = self.fabrica.crear_vid("cabernet sauvignon")
        self.assertIsInstance(vid, CabernetSauvignon)

    def test_lanza_error_si_varietal_no_existe(self):
        with self.assertRaises(ValueError):
            self.fabrica.crear_vid("bonarda")

if __name__ == '__main__':
    unittest.main()