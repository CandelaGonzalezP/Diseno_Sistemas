from abc import ABC, abstractmethod

class Cultivo(ABC):
    """
    Clase base abstracta que representa cualquier tipo de cultivo plantable.
    
    Define la interfaz común para todos los cultivos del sistema forestal,
    incluyendo árboles y hortalizas.
    
    Attributes:
        _litros_agua_absorbidos: Cantidad total de agua absorbida por el cultivo.
        _metros_cuadrados_requeridos: Superficie necesaria para plantar el cultivo.
    """

    def __init__(self, agua_inicial: float = 0.0):
        """
        Inicializa un nuevo cultivo con agua inicial.
        
        Args:
            agua_inicial: Cantidad inicial de agua absorbida en litros. Por defecto 0.0.
        """
        self._litros_agua_absorbidos = agua_inicial
        self._metros_cuadrados_requeridos = 0.0

    @property
    def litros_agua_absorbidos(self) -> float:
        """
        Obtiene la cantidad total de agua absorbida por el cultivo.
        
        Returns:
            Cantidad de agua en litros.
        """
        return self._litros_agua_absorbidos

    @property
    def metros_cuadrados_requeridos(self) -> float:
        """
        Obtiene la superficie requerida para plantar el cultivo.
        
        Returns:
            Superficie en metros cuadrados.
        """
        return self._metros_cuadrados_requeridos

    @abstractmethod
    def crecer(self, litros_agua: float):
        """
        Define el comportamiento de crecimiento del cultivo al ser regado.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
            
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        pass

    @abstractmethod
    def get_tipo(self) -> str:
        """
        Devuelve el nombre o tipo del cultivo.
        
        Returns:
            Nombre del tipo de cultivo como cadena de texto.
            
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        pass
