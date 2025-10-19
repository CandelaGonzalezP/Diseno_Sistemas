from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entidades.terrenos.finca import Finca
    from servicios.personal.contratista import Contratista

class EstrategiaCosecha(ABC):
    @abstractmethod
    def cosechar_finca(self, contratista: Contratista, finca: Finca):
        pass

class CosechaManual(EstrategiaCosecha):
    def cosechar_finca(self, contratista: Contratista, finca: Finca):
        print(f"-> {contratista.nombre} está aplicando 'Cosecha Manual': cuidadosa y selectiva.")
        finca.cosechar()

class CosechaMecanica(EstrategiaCosecha):
    def cosechar_finca(self, contratista: Contratista, finca: Finca):
        print(f"-> {contratista.nombre} está aplicando 'Cosecha Mecánica': rápida y a gran escala.")
        finca.cosechar()