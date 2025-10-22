class Tierra:
    """
    Representa un terreno catastral con su información legal y física.
    
    Gestiona los datos catastrales de un terreno forestal, incluyendo su
    identificación única (padrón), superficie y ubicación. Incluye validación
    interna para garantizar datos consistentes.
    
    Attributes:
        _padron_catastral: Identificador único del terreno en el registro catastral.
        _superficie_m2: Superficie del terreno en metros cuadrados (debe ser positiva).
        _domicilio: Dirección o ubicación geográfica del terreno.
    
    Raises:
        ValueError: Si la superficie es menor o igual a cero durante la inicialización.
    """
    
    def __init__(self, padron_catastral: str, superficie_m2: float, domicilio: str):
        """
        Inicializa un nuevo terreno con validación de superficie.
        
        Args:
            padron_catastral: Identificador catastral único del terreno.
            superficie_m2: Superficie del terreno en metros cuadrados (debe ser > 0).
            domicilio: Dirección o ubicación geográfica del terreno.
        
        Raises:
            ValueError: Si superficie_m2 es menor o igual a cero.
        """
        if superficie_m2 <= 0:
            raise ValueError("La superficie debe ser un número positivo.")
        
        self._padron_catastral = padron_catastral
        self._superficie_m2 = superficie_m2
        self._domicilio = domicilio

    @property
    def padron_catastral(self) -> str:
        """
        Obtiene el padrón catastral del terreno.
        
        Returns:
            Identificador catastral único del terreno.
        """
        return self._padron_catastral

    @property
    def superficie_m2(self) -> float:
        """
        Obtiene la superficie del terreno en metros cuadrados.
        
        Returns:
            Superficie en metros cuadrados.
        """
        return self._superficie_m2

    @property
    def domicilio(self) -> str:
        """
        Obtiene el domicilio o ubicación del terreno.
        
        Returns:
            Dirección geográfica del terreno.
        """
        return self._domicilio

    def set_superficie(self, nueva_superficie_m2: float):
        """
        Modifica la superficie del terreno con validación.
        
        Actualiza la superficie del terreno validando que el nuevo valor
        sea positivo. Cumple con el criterio de aceptación de US-001.
        
        Args:
            nueva_superficie_m2: Nueva superficie en metros cuadrados (debe ser > 0).
        
        Raises:
            ValueError: Si nueva_superficie_m2 es menor o igual a cero.
        """
        if nueva_superficie_m2 <= 0:
            raise ValueError("La superficie debe ser un número positivo.")
        self._superficie_m2 = nueva_superficie_m2
        print(f"INFO: La superficie del padrón {self._padron_catastral} se actualizó a {self._superficie_m2} m².")
