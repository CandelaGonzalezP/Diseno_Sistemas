import unittest
import sys
import os

# Adds the 'src' directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now the imports will work correctly
from entidades.organizacion.inv import INV
from servicios.creacion.finca_builder import FincaBuilder
from entidades.cultivos.vid import Malbec

class TestObserverSingleton(unittest.TestCase):
    def test_inv_es_singleton(self):
        inv1 = INV()
        inv2 = INV()
        self.assertIs(inv1, inv2, "INV is not implementing Singleton correctly.")

    def test_inv_es_notificado_como_observer(self):
        inv = INV()
        finca = FincaBuilder(10).build()
        finca.attach(inv)
        
        cosechas_antes = inv.cosechas_registradas
        finca.plantar_vid(Malbec())
        finca.cosechar()
        cosechas_despues = inv.cosechas_registradas
        
        self.assertEqual(cosechas_despues, cosechas_antes + 1, "The observer was not notified.")

if __name__ == '__main__':
    unittest.main()