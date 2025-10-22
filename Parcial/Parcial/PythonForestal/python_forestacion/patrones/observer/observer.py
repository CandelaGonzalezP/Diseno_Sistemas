from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    Interfaz del patrón Observer para objetos que reciben notificaciones de eventos.
    
    Define el contrato que deben cumplir todos los observadores en el sistema.
    Los observadores se suscriben a objetos Observable y reciben notificaciones
    automáticas cuando ocurren eventos mediante el método actualizar().
    
    Esta clase abstracta genérica garantiza type-safety, asegurando que el tipo
    de evento recibido coincida con el tipo esperado por el observador.
    
    En el sistema de riego automatizado, ControlRiegoTask implementa Observer[float]
    para recibir lecturas de los sensores de temperatura y humedad.
    
    Type Parameters:
        T: Tipo de dato del evento que será recibido por el observador.

    """
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método abstracto que recibe notificaciones cuando ocurre un evento.
        
        Este método es llamado automáticamente por el Observable cuando se invoca
        notificar_observadores(). Las implementaciones concretas deben definir
        la lógica de respuesta al evento recibido.
        
        En el sistema de riego, ControlRiegoTask implementa este método para:
        - Actualizar valores de temperatura/humedad
        - Evaluar condiciones de riego
        - Activar riego automático si las condiciones se cumplen
        
        Args:
            evento: Dato del evento notificado (debe ser de tipo T).
        
        """
        pass