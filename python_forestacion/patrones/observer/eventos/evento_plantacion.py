from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....entidades.cultivos.cultivo import Cultivo
    from ....entidades.terrenos.plantacion import Plantacion


class TipoEventoPlantacion(Enum):
    """
    Enumeración de tipos de eventos que pueden ocurrir en una plantación.
    
    Define los diferentes eventos del ciclo de vida de una plantación que
    podrían ser monitoreados por observadores en el sistema.
    
    Attributes:
        CULTIVO_PLANTADO: Se plantó un nuevo cultivo en la plantación.
        RIEGO_REALIZADO: Se completó una operación de riego.
        CULTIVO_COSECHADO: Se cosechó un cultivo de la plantación.
        FUMIGACION_APLICADA: Se aplicó un plaguicida a la plantación.
        AGUA_AGOTADA: El agua disponible cayó por debajo del umbral crítico.
        SUPERFICIE_INSUFICIENTE: No hay suficiente superficie para plantar.
    """
    CULTIVO_PLANTADO = auto()
    RIEGO_REALIZADO = auto()
    CULTIVO_COSECHADO = auto()
    FUMIGACION_APLICADA = auto()
    AGUA_AGOTADA = auto()
    SUPERFICIE_INSUFICIENTE = auto()


@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación agrícola.
    
    Encapsula información completa sobre eventos del ciclo de vida de una
    plantación, permitiendo un sistema de logging, auditoría y notificaciones
    más robusto que el actual.
    
    Esta clase es opcional y actualmente no se utiliza en el sistema principal.
    Se proporciona como extensión para futuras implementaciones que requieran:
    - Logging detallado de operaciones
    - Auditoría completa de cambios en plantaciones
    - Sistema de notificaciones a múltiples observadores
    - Dashboard de monitoreo en tiempo real
    - Análisis histórico de operaciones
    

    Attributes:
        tipo: Tipo de evento que ocurrió en la plantación.
        plantacion: Plantación donde ocurrió el evento.
        timestamp: Momento exacto del evento.
        descripcion: Descripción textual del evento para logging.
        cultivo_relacionado: Cultivo involucrado en el evento (opcional).
        datos_adicionales: Diccionario con información adicional (opcional).
    """
    tipo: TipoEventoPlantacion
    plantacion: 'Plantacion'
    timestamp: datetime
    descripcion: str
    cultivo_relacionado: 'Cultivo' = None
    datos_adicionales: dict = None

    def __str__(self) -> str:
        """
        Representación en cadena legible del evento.
        
        Returns:
            Cadena formateada con tipo, plantación, timestamp y descripción.

        """
        plantacion_nombre = self.plantacion.nombre if self.plantacion else "Desconocida"
        timestamp_str = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        resultado = (f"[{self.tipo.name}] Plantación '{plantacion_nombre}' - {timestamp_str}\n"
                    f"Descripción: {self.descripcion}")
        
        if self.cultivo_relacionado:
            resultado += f"\nCultivo: {self.cultivo_relacionado.get_tipo()}"
        
        if self.datos_adicionales:
            resultado += f"\nDatos adicionales: {self.datos_adicionales}"
        
        return resultado

    def es_evento_critico(self) -> bool:
        """
        Determina si el evento requiere atención inmediata.
        
        Los eventos críticos son aquellos que indican problemas o situaciones
        que requieren intervención del operador del sistema.
        
        Returns:
            True si es evento crítico (agua agotada o superficie insuficiente).

        """
        return self.tipo in {
            TipoEventoPlantacion.AGUA_AGOTADA,
            TipoEventoPlantacion.SUPERFICIE_INSUFICIENTE
        }

    def es_evento_operacional(self) -> bool:
        """
        Determina si el evento es parte de operaciones normales.
        
        Los eventos operacionales son operaciones rutinarias del sistema
        que no requieren atención especial.
        
        Returns:
            True si es evento operacional (plantado, riego, cosecha, fumigación).

        """
        return self.tipo in {
            TipoEventoPlantacion.CULTIVO_PLANTADO,
            TipoEventoPlantacion.RIEGO_REALIZADO,
            TipoEventoPlantacion.CULTIVO_COSECHADO,
            TipoEventoPlantacion.FUMIGACION_APLICADA
        }

    @staticmethod
    def crear_evento_plantado(plantacion: 'Plantacion', cultivo: 'Cultivo') -> 'EventoPlantacion':
        """
        Factory method para crear un evento de plantación de cultivo.
        
        Args:
            plantacion: Plantación donde se plantó el cultivo.
            cultivo: Cultivo que fue plantado.
        
        Returns:
            EventoPlantacion configurado para plantación de cultivo.

        """
        return EventoPlantacion(
            tipo=TipoEventoPlantacion.CULTIVO_PLANTADO,
            plantacion=plantacion,
            timestamp=datetime.now(),
            descripcion=f"Se plantó {cultivo.get_tipo()} en la plantación",
            cultivo_relacionado=cultivo
        )

    @staticmethod
    def crear_evento_riego(plantacion: 'Plantacion', litros_consumidos: float) -> 'EventoPlantacion':
        """
        Factory method para crear un evento de riego.
        
        Args:
            plantacion: Plantación que fue regada.
            litros_consumidos: Cantidad de agua utilizada en el riego.
        
        Returns:
            EventoPlantacion configurado para riego.
 
        """
        return EventoPlantacion(
            tipo=TipoEventoPlantacion.RIEGO_REALIZADO,
            plantacion=plantacion,
            timestamp=datetime.now(),
            descripcion=f"Se realizó riego con {litros_consumidos} litros",
            datos_adicionales={"litros_consumidos": litros_consumidos}
        )

    @staticmethod
    def crear_evento_agua_agotada(plantacion: 'Plantacion', agua_disponible: float) -> 'EventoPlantacion':
        """
        Factory method para crear un evento de agua agotada (crítico).
        
        Args:
            plantacion: Plantación con agua agotada.
            agua_disponible: Cantidad de agua restante (debajo del umbral).
        
        Returns:
            EventoPlantacion configurado para agua agotada.

        """
        return EventoPlantacion(
            tipo=TipoEventoPlantacion.AGUA_AGOTADA,
            plantacion=plantacion,
            timestamp=datetime.now(),
            descripcion=f"ALERTA: Agua agotada. Disponible: {agua_disponible}L",
            datos_adicionales={"agua_disponible": agua_disponible}
        )