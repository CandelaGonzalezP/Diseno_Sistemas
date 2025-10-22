from .forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua para completar una operación.
    
    Se utiliza cuando se intenta realizar un riego u otra operación que requiere
    agua, pero la plantación no tiene suficientes recursos hídricos disponibles.
    Proporciona información detallada sobre la cantidad requerida versus la disponible.
    
    Attributes:
        _requerida: Cantidad de agua necesaria para la operación en litros.
        _disponible: Cantidad de agua actualmente disponible en litros.
    """
    
    def __init__(self, agua_requerida: float, agua_disponible: float):
        """
        Inicializa una excepción de agua agotada con cantidades específicas.
        
        Args:
            agua_requerida: Cantidad de agua necesaria en litros.
            agua_disponible: Cantidad de agua disponible en litros.
        """
        self._requerida = agua_requerida
        self._disponible = agua_disponible
       
        mensaje = (f"Recursos hídricos insuficientes. Requerido: {self._requerida:.2f}L, "
                   f"Disponible: {self._disponible:.2f}L.")
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Returns:
            Mensaje amigable indicando falta de agua.
        """
        return "Agua insuficiente para completar el riego."

    def get_agua_requerida(self) -> float:
        """
        Obtiene la cantidad de agua que se requería para la operación.
        
        Returns:
            Cantidad de agua requerida en litros.
        """
        return self._requerida

    def get_agua_disponible(self) -> float:
        """
        Obtiene la cantidad de agua actualmente disponible.
        
        Returns:
            Cantidad de agua disponible en litros.
        """
        return self._disponible
