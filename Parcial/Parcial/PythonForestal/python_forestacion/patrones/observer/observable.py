from typing import List, TypeVar, Generic
from .observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """
    Implementación del patrón Observer que permite notificar cambios a múltiples observadores.
    
    Esta clase genérica permite a los objetos Observable notificar a sus observadores registrados
    cuando ocurre un evento. Utiliza generics para garantizar type-safety, asegurando que el tipo
    de evento notificado coincida con el tipo esperado por los observadores.
    
    El patrón Observer es utilizado en el sistema de riego automatizado, donde los sensores
    de temperatura y humedad actúan como Observable[float], notificando lecturas al controlador
    de riego que actúa como Observer[float].
    
    Type Parameters:
        T: Tipo de dato del evento que será notificado a los observadores.
    
    Attributes:
        _observadores: Lista de observadores suscritos a este observable.
    
    """

    def __init__(self):
        """
        Inicializa un nuevo Observable con lista vacía de observadores.
        """
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Registra un observador para recibir notificaciones de eventos.
        
        El observador solo se agrega si no está ya registrado, evitando duplicados.
        Una vez registrado, recibirá notificaciones cada vez que se llame a
        notificar_observadores().
        
        Args:
            observador: Instancia de Observer[T] que será notificada de eventos.

        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def quitar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista de suscritos.
        
        Después de quitarlo, el observador ya no recibirá notificaciones de eventos.
        Si el observador no está registrado, lanza ValueError.
        
        Args:
            observador: Instancia de Observer[T] a eliminar.
        
        Raises:
            ValueError: Si el observador no está en la lista de observadores.
        """
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores registrados sobre un evento ocurrido.
        
        Itera sobre la lista de observadores y llama al método actualizar() de cada uno,
        pasando el evento como parámetro. El evento debe ser del tipo T especificado
        en la declaración del Observable.
        
        En el sistema de riego, este método es llamado cada vez que un sensor lee
        un nuevo valor (temperatura o humedad), notificando al controlador de riego.
        
        Args:
            evento: Dato del evento a notificar (debe ser de tipo T).
        

        """
        print(f"OBSERVABLE: Notificando a {len(self._observadores)} observador(es)...")
        for observador in self._observadores:
            observador.actualizar(evento)