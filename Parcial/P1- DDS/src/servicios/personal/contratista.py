from entidades.terrenos.finca import Finca
from servicios.negocio.estrategias_cosecha import EstrategiaCosecha, CosechaManual

class Contratista:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._estrategia: EstrategiaCosecha = CosechaManual()

    def set_estrategia(self, estrategia: EstrategiaCosecha):
        print(f"\nINFO: El contratista {self.nombre} cambia su estrategia a '{estrategia.__class__.__name__}'.")
        self._estrategia = estrategia

    def ejecutar_cosecha(self, finca: Finca):
        self._estrategia.cosechar_finca(self, finca)