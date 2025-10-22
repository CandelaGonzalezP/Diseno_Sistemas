from typing import Dict, Callable
from ...entidades.cultivos.cultivo import Cultivo
from ...entidades.cultivos.pino import Pino
from ...entidades.cultivos.olivo import Olivo
from ...entidades.cultivos.lechuga import Lechuga
from ...entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    """
    Implementa el patrón Factory Method para crear instancias de cultivos.
    
    Centraliza la lógica de creación de diferentes tipos de cultivos,
    desacoplando el código cliente de las clases concretas mediante
    el uso de métodos estáticos dedicados en lugar de lambdas.
    
    El patrón Factory Method cumple con:
    - Open/Closed Principle: Extensible sin modificar código existente
    - Dependency Inversion: Cliente depende de abstracción (Cultivo)
    - Single Responsibility: Solo responsable de crear cultivos
    
    Attributes:
        _factories: Diccionario que mapea nombres de especies a métodos de creación.
    
    Example:
        >>> cultivo = CultivoFactory.crear_cultivo("Pino")
        >>> isinstance(cultivo, Pino)
        True
    """
    
    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Crea una instancia de Pino con configuración por defecto.
        
        Returns:
            Nueva instancia de Pino con variedad "Parana".
        """
        return Pino()
    
    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Crea una instancia de Olivo con configuración por defecto.
        
        Returns:
            Nueva instancia de Olivo con tipo de aceituna ARBEQUINA.
        """
        return Olivo()
    
    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Crea una instancia de Lechuga con configuración por defecto.
        
        Returns:
            Nueva instancia de Lechuga con variedad "Invernadero".
        """
        return Lechuga()
    
    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Crea una instancia de Zanahoria con configuración por defecto.
        
        Returns:
            Nueva instancia de Zanahoria tipo regular (no baby).
        """
        return Zanahoria()
    
    _factories: Dict[str, Callable[[], Cultivo]] = {
        "pino": _crear_pino.__func__,           
        "olivo": _crear_olivo.__func__,         
        "lechuga": _crear_lechuga.__func__,     
        "zanahoria": _crear_zanahoria.__func__  
    }

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea una instancia de cultivo según la especie especificada.
        
        Método principal del Factory que actúa como punto de entrada único
        para la creación de cultivos. Utiliza dispatch mediante diccionario
        para delegar la creación al método específico correspondiente.
        
        Este diseño permite agregar nuevos tipos de cultivos sin modificar
        el código cliente, cumpliendo con el Open/Closed Principle.
        
        Args:
            especie: Nombre del tipo de cultivo a crear. No es sensible a
                    mayúsculas/minúsculas. Valores válidos: "Pino", "Olivo",
                    "Lechuga", "Zanahoria".
        
        Returns:
            Instancia de Cultivo del tipo solicitado (Pino, Olivo, Lechuga o Zanahoria).
        
        Raises:
            ValueError: Si la especie solicitada no está registrada en el factory.
        
        Example:
            >>> pino = CultivoFactory.crear_cultivo("Pino")
            >>> olivo = CultivoFactory.crear_cultivo("olivo")  # Case insensitive
            >>> lechuga = CultivoFactory.crear_cultivo("LECHUGA")
        
        Note:
            El factory retorna el tipo base Cultivo para mantener el desacoplamiento,
            aunque internamente crea instancias de tipos concretos.
        """
        especie_lower = especie.lower()
        
        if especie_lower not in CultivoFactory._factories:
            raise ValueError(
                f"Especie de cultivo desconocida: '{especie}'. "
                f"Especies válidas: {', '.join(CultivoFactory._factories.keys())}"
            )
        
        return CultivoFactory._factories[especie_lower]()