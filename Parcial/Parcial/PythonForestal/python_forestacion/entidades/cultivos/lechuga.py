from .hortaliza import Hortaliza
from ...constantes import SUPERFICIE_LECHUGA_M2

class Lechuga(Hortaliza):
    """
    Representa una hortaliza de tipo lechuga con variedad específica.
    
    La lechuga es una hortaliza de hoja verde que típicamente se cultiva
    en invernaderos y requiere riego constante.
    
    Attributes:
        _variedad: Tipo de lechuga (ej. Invernadero, Crespa, Mantecosa).
    """

    def __init__(self, variedad: str = "Invernadero"):
        """
        Inicializa una nueva lechuga con su variedad.
        
        Args:
            variedad: Tipo de lechuga a cultivar. Por defecto "Invernadero".
        """
        super().__init__(agua_inicial=1.0)
        self._variedad = variedad
        self._metros_cuadrados_requeridos = SUPERFICIE_LECHUGA_M2

    @property
    def variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.
        
        Returns:
            Nombre de la variedad como cadena de texto.
        """
        return self._variedad

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento de la lechuga al recibir agua.
        
        Incrementa el agua absorbida y muestra información del riego.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        super().crecer(litros_agua)
        print(f"La Lechuga variedad '{self.variedad}' absorbió {litros_agua}L de agua.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Lechuga".
        """
        return "Lechuga"
