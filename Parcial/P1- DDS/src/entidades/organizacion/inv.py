from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Se usan rutas absolutas desde 'src'
    from entidades.terrenos.finca import Finca, Subject

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

class INV(Observer):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("INFO: Creando instancia única del INV.")
            cls._instance = super(INV, cls).__new__(cls)
            cls._instance.cosechas_registradas = 0
        return cls._instance

    def update(self, subject: Finca):
        self.cosechas_registradas += 1
        print(f"**[INV]** Notificación recibida: Se realizó una cosecha en la finca '{subject.nombre}'. Total de cosechas registradas: {self.cosechas_registradas}.")