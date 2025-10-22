from .cultivo import Cultivo

class Hortaliza(Cultivo):
    """
    Clase base para cultivos de tipo hortaliza.
    
    Extiende la funcionalidad de Cultivo para hortalizas, que tienen
    un comportamiento de crecimiento más simple que los árboles.
    """

    def __init__(self, agua_inicial: float = 0.0):
        """
        Inicializa una nueva hortaliza.
        
        Args:
            agua_inicial: Cantidad inicial de agua absorbida en litros. Por defecto 0.0.
        """
        super().__init__(agua_inicial)
    
    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento de la hortaliza absorbiendo agua.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        self._litros_agua_absorbidos += litros_agua
