from .hortaliza import Hortaliza
from ...constantes import SUPERFICIE_ZANAHORIA_M2

class Zanahoria(Hortaliza):
    """
    Representa una hortaliza de tipo zanahoria.
    
    La zanahoria puede ser de tipo normal o baby carrot, con diferentes
    características según su tipo.
    
    Attributes:
        _es_baby: Indica si es una zanahoria tipo baby carrot.
    """

    def __init__(self, es_baby: bool = False):
        """
        Inicializa una nueva zanahoria.
        
        Args:
            es_baby: Indica si es baby carrot (True) o normal (False). Por defecto False.
        """
        super().__init__(agua_inicial=0.0)
        self._es_baby = es_baby
        self._metros_cuadrados_requeridos = SUPERFICIE_ZANAHORIA_M2

    @property
    def es_baby(self) -> bool:
        """
        Verifica si la zanahoria es tipo baby carrot.
        
        Returns:
            True si es baby carrot, False si es normal.
        """
        return self._es_baby

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento de la zanahoria al recibir agua.
        
        Incrementa el agua absorbida y muestra información según el tipo
        de zanahoria (baby o normal).
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        super().crecer(litros_agua)
        tipo_zanahoria = "Baby" if self.es_baby else "Normal"
        print(f"La Zanahoria '{tipo_zanahoria}' absorbió {litros_agua}L de agua.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Zanahoria".
        """
        return "Zanahoria"
