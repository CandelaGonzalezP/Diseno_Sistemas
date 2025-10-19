from entidades.terrenos.finca import Finca

class FincaBuilder:
    def __init__(self, hectareas: int):
        self.hectareas = hectareas
        self.nombre = "Finca Sin Nombre"
        self.tipo_suelo = "Franco Arcilloso"

    def con_nombre(self, nombre: str):
        self.nombre = nombre
        return self

    def con_tipo_suelo(self, tipo_suelo: str):
        self.tipo_suelo = tipo_suelo
        return self

    def build(self) -> Finca:
        print(f"INFO: Finca '{self.nombre}' construida con éxito.")
        return Finca(self)