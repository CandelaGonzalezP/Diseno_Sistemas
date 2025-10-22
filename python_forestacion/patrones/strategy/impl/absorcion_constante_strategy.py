from datetime import date
from ..absorcion_agua_strategy import AbsorcionAguaStrategy
from ....entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua constante para cultivos hortícolas.
    
    Implementa el patrón Strategy para calcular la absorción de agua de cultivos
    que mantienen un consumo hídrico constante independientemente de la estación
    del año o condiciones ambientales.
    
    Esta estrategia es utilizada por hortalizas como Lechuga (1L) y Zanahoria (2L),
    que requieren riego uniforme durante todo su ciclo de crecimiento.
    
    En el sistema, esta estrategia se inyecta en los servicios de cultivos hortícolas
    durante su inicialización, cumpliendo con el principio de Dependency Inversion.
    
    Attributes:
        _cantidad: Cantidad fija de litros de agua que el cultivo absorbe por riego.

    """

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia con una cantidad fija de absorción.
        
        Args:
            cantidad_constante: Cantidad de litros que el cultivo absorbe por riego.
                               Debe ser un valor positivo.

        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, cultivo: Cultivo) -> int:
        """
        Calcula la absorción de agua retornando siempre la cantidad constante.
        
        A diferencia de AbsorcionSeasonalStrategy, este método ignora la fecha
        y las condiciones ambientales, retornando siempre el mismo valor definido
        en el constructor.
        
        Args:
            fecha: Fecha del riego (no utilizada en esta estrategia).
            cultivo: Instancia del cultivo a regar (no utilizada en esta estrategia).
        
        Returns:
            Cantidad constante de litros de agua absorbidos.
        """
        return self._cantidad