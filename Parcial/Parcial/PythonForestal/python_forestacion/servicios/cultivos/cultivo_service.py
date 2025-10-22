from abc import ABC, abstractmethod
from ...entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """
    Clase base abstracta para todos los servicios de cultivos del sistema.
    
    Define el contrato que deben cumplir todos los servicios de cultivos,
    estableciendo las operaciones fundamentales de plantación y cosecha.
    
    Esta clase implementa el patrón Template Method al nivel de interfaz,
    forzando a las subclases a implementar operaciones específicas mientras
    mantiene una estructura consistente en toda la jerarquía de servicios.
    
    """
    
    @abstractmethod
    def plantar(self, cultivo: Cultivo):
        """
        Método abstracto para plantar un cultivo.
        
        Las subclases deben implementar la lógica específica de plantación
        para su tipo de cultivo, incluyendo validaciones, registro de eventos,
        y cualquier inicialización necesaria.
        
        Args:
            cultivo: Instancia del cultivo a plantar.

        """
        pass

    @abstractmethod
    def cosechar(self, cultivo: Cultivo):
        """
        Método abstracto para cosechar un cultivo.
        
        Las subclases deben implementar la lógica específica de cosecha
        para su tipo de cultivo, especificando qué se extrae (madera, aceitunas,
        hojas, raíces) y cualquier procesamiento post-cosecha.
        
        Args:
            cultivo: Instancia del cultivo a cosechar.

        """
        pass