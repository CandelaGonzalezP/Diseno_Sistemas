from .arbol import Arbol
from ...constantes import SUPERFICIE_PINO_M2, CRECIMIENTO_PINO_POR_RIEGO_M

class Pino(Arbol):
    """
    Representa un árbol de pino con variedad específica.
    
    El pino es un árbol maderable que requiere superficie considerable
    y crece de manera constante con cada riego.
    
    Attributes:
        _variedad: Tipo de pino (ej. Paraná, Elliott, Taeda).
    """

    def __init__(self, anios: int = 0, variedad: str = "Parana"):
        """
        Inicializa un nuevo pino con sus características.
        
        Args:
            anios: Edad inicial del pino en años. Por defecto 0.
            variedad: Tipo de pino a plantar. Por defecto "Parana".
        """
        super().__init__(anios=anios, agua_inicial=2.0, altura_inicial=1.0)
        self._variedad = variedad
        self._metros_cuadrados_requeridos = SUPERFICIE_PINO_M2

    @property
    def variedad(self) -> str:
        """
        Obtiene la variedad del pino.
        
        Returns:
            Nombre de la variedad como cadena de texto.
        """
        return self._variedad

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento del pino al recibir agua.
        
        Incrementa tanto el agua absorbida como la altura del árbol
        según la constante de crecimiento definida.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        self._litros_agua_absorbidos += litros_agua
        self._altura_metros += CRECIMIENTO_PINO_POR_RIEGO_M
        print(f"El Pino variedad '{self.variedad}' creció a {self.altura_metros:.2f}m.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Pino".
        """
        return "Pino"
