from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie para plantar un cultivo.
    
    Se utiliza cuando se intenta plantar un cultivo pero la plantación no tiene
    suficiente superficie disponible. Proporciona información detallada sobre la
    superficie requerida por el cultivo versus la superficie disponible en la plantación.
    
    Attributes:
        _requerida: Superficie necesaria para el cultivo en metros cuadrados.
        _disponible: Superficie actualmente disponible en metros cuadrados.
    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa una excepción de superficie insuficiente con valores específicos.
        
        Args:
            superficie_requerida: Superficie necesaria en metros cuadrados.
            superficie_disponible: Superficie disponible en metros cuadrados.
        """
        self._requerida = superficie_requerida
        self._disponible = superficie_disponible
       
        mensaje = (f"Superficie insuficiente. Requerido: {self._requerida:.2f} m², "
                   f"Disponible: {self._disponible:.2f} m².")
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Returns:
            Mensaje amigable indicando falta de superficie.
        """
        return "Superficie insuficiente para plantar."

    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie que se requería para plantar el cultivo.
        
        Returns:
            Superficie requerida en metros cuadrados.
        """
        return self._requerida

    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie actualmente disponible en la plantación.
        
        Returns:
            Superficie disponible en metros cuadrados.
        """
        return self._disponible
