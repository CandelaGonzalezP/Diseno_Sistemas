from dataclasses import dataclass
from .tierra import Tierra
from .plantacion import Plantacion

@dataclass
class RegistroForestal:
    """
    Entidad principal que vincula un terreno con su plantación.
    
    Representa el registro oficial completo de una propiedad forestal,
    incluyendo datos del propietario, avalúo fiscal, información del
    terreno y detalles de la plantación asociada.
    
    Attributes:
        propietario: Nombre completo del propietario del terreno.
        avaluo_fiscal: Valor fiscal del terreno para fines impositivos.
        tierra: Objeto Tierra con la información catastral del terreno.
        plantacion: Objeto Plantacion con los cultivos y trabajadores.
    """
    
    propietario: str
    avaluo_fiscal: float
    tierra: Tierra
    plantacion: Plantacion

    def mostrar_datos(self):
        """
        Imprime en consola los datos del registro con formato específico.
        
        Muestra de manera estructurada toda la información del registro
        forestal, incluyendo datos catastrales, propietario, avalúo y
        cantidad de cultivos. Cumple con el criterio de aceptación de US-003.
        """
        print("\nREGISTRO FORESTAL")
        print("=" * 17)
        print(f"Padron:      {self.tierra.padron_catastral}")
        print(f"Propietario: {self.propietario}")
        print(f"Avaluo:      {self.avaluo_fiscal}")
        print(f"Domicilio:   {self.tierra.domicilio}")
        print(f"Superficie:  {self.tierra.superficie_m2}")
        print(f"Cantidad de cultivos plantados: {self.plantacion.get_cantidad_cultivos()}")  # pylint: disable=no-member
        print("=" * 17)