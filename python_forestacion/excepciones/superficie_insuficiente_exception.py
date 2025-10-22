from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie para plantar un cultivo.
    
    Se utiliza cuando se intenta plantar un cultivo pero la plantación no tiene
    suficiente superficie disponible. Proporciona información detallada sobre:
    - Superficie requerida por el cultivo
    - Superficie disponible en la plantación
    - Diferencia (déficit de superficie)
    
    Esta excepción cumple con el criterio de aceptación de US-004 que especifica:
    "Si no hay superficie, lanzar SuperficieInsuficienteException".
    
    Attributes:
        _requerida: Superficie necesaria para el cultivo en metros cuadrados.
        _disponible: Superficie actualmente disponible en metros cuadrados.
 

    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa una excepción de superficie insuficiente con valores específicos.
        
        Construye mensajes técnicos detallados incluyendo las cantidades exactas
        de superficie requerida versus disponible para facilitar el diagnóstico.
        
        Args:
            superficie_requerida: Superficie necesaria en metros cuadrados (debe ser > 0).
            superficie_disponible: Superficie disponible en metros cuadrados (debe ser >= 0).

        """
        self._requerida = superficie_requerida
        self._disponible = superficie_disponible
       
        mensaje = (
            f"Superficie insuficiente. "
            f"Requerido: {self._requerida:.2f} m², "
            f"Disponible: {self._disponible:.2f} m². "
            f"Déficit: {(self._requerida - self._disponible):.2f} m²"
        )
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Proporciona un mensaje amigable sin detalles técnicos para
        interfaces de usuario o reportes orientados a usuarios no técnicos.
        
        Returns:
            Mensaje simplificado indicando falta de superficie.
  
        """
        return "Superficie insuficiente para plantar."

    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie que se requería para plantar el cultivo.
        
        Útil para cálculos de expansión o re-planificación de plantaciones.
        
        Returns:
            Superficie requerida en metros cuadrados.
   
        """
        return self._requerida

    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie actualmente disponible en la plantación.
        
        Permite al código cliente tomar decisiones sobre cuántos cultivos
        alternativos podrían plantarse con la superficie disponible.
        
        Returns:
            Superficie disponible en metros cuadrados.

        """
        return self._disponible
    
    def get_deficit(self) -> float:
        """
        Calcula el déficit de superficie (cuánto falta).
        
        Returns:
            Diferencia entre requerido y disponible en metros cuadrados.
  
        """
        return self._requerida - self._disponible