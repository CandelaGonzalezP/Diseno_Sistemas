from __future__ import annotations
from abc import ABC
from typing import List, TYPE_CHECKING

# Se usan rutas absolutas desde 'src'
from entidades.cultivos.vid import Vid

if TYPE_CHECKING:
    from entidades.organizacion.inv import Observer
    from servicios.creacion.finca_builder import FincaBuilder

class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Finca(Subject):
    def __init__(self, builder: FincaBuilder):
        super().__init__()
        self.nombre = builder.nombre
        self.hectareas = builder.hectareas
        self.tipo_suelo = builder.tipo_suelo
        self.vides: List[Vid] = []

    def plantar_vid(self, vid: Vid):
        self.vides.append(vid)
        print(f"INFO: Se ha plantado una vid de '{vid.get_varietal()}' en la finca '{self.nombre}'.")

    def cosechar(self):
        print(f"\n--- Cosecha iniciada en la finca '{self.nombre}' ---")
        if not self.vides:
            print("ADVERTENCIA: No hay vides para cosechar.")
            return
        print(f"INFO: Cosecha finalizada. {len(self.vides)} hileras procesadas.")
        self.notify()

    def __str__(self):
        return f"Finca '{self.nombre}' de {self.hectareas} hectáreas."