from ...entidades.terrenos.tierra import Tierra

class TierraService:
    """
    Servicio para creación y gestión de terrenos catastrales.
    
    Maneja la creación de objetos Tierra con validación de datos.
    """
   
    def crear_tierra(self, padron: str, superficie: float, domicilio: str) -> Tierra:
        """
        Crea una nueva instancia de Tierra con datos catastrales.
        
        Args:
            padron: Identificador único catastral.
            superficie: Superficie en metros cuadrados.
            domicilio: Ubicación física del terreno.
        
        Returns:
            Instancia de Tierra creada.
        """
        print(f"SERVICIO: Creando registro para tierra con padrón {padron}.")
        return Tierra(padron_catastral=padron, superficie_m2=superficie, domicilio=domicilio)