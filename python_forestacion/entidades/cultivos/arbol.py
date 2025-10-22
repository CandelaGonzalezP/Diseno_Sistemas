from abc import abstractmethod
from .cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base abstracta para cultivos de tipo árbol.
    
    Extiende la funcionalidad de Cultivo añadiendo características específicas
    de árboles como edad y altura.
    
    Attributes:
        _anios: Edad del árbol en años.
        _altura_metros: Altura actual del árbol en metros.
    """

    def __init__(self, anios: int = 0, agua_inicial: float = 0.0, altura_inicial: float = 0.0):
        """
        Inicializa un nuevo árbol con sus características.
        
        Args:
            anios: Edad inicial del árbol en años. Por defecto 0.
            agua_inicial: Cantidad inicial de agua absorbida en litros. Por defecto 0.0.
            altura_inicial: Altura inicial del árbol en metros. Por defecto 0.0.
        """
        super().__init__(agua_inicial)
        self._anios = anios
        self._altura_metros = altura_inicial

    @property
    def anios(self) -> int:
        """
        Obtiene la edad del árbol.
        
        Returns:
            Edad en años.
        """
        return self._anios

    @property
    def altura_metros(self) -> float:
        """
        Obtiene la altura actual del árbol.
        
        Returns:
            Altura en metros.
        """
        return self._altura_metros

    @abstractmethod
    def crecer(self, litros_agua: float):
        """
        Define el comportamiento de crecimiento específico del árbol al ser regado.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
            
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        pass