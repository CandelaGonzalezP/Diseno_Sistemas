"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\observer.py
# ================================================================================

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

