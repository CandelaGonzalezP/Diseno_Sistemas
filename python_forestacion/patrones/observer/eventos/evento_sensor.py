from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class TipoSensor(Enum):
    """
    Enumeración de tipos de sensores ambientales del sistema de riego.
    
    Define los tipos de sensores que pueden generar eventos en el
    sistema de monitoreo automatizado.
    
    Attributes:
        TEMPERATURA: Sensor que mide temperatura ambiental en °C.
        HUMEDAD: Sensor que mide humedad relativa del aire en %.
    """
    TEMPERATURA = auto()
    HUMEDAD = auto()


@dataclass
class EventoSensor:
    """
    Representa un evento generado por un sensor ambiental.
    
    Encapsula la información completa de una lectura de sensor, incluyendo
    el tipo de sensor, el valor medido y el timestamp de la lectura.
    
    Esta clase es opcional y actualmente no se utiliza en el sistema,
    ya que los sensores notifican directamente valores float mediante
    Observable[float]. Sin embargo, se proporciona como ejemplo de cómo
    se podrían estructurar eventos más complejos en futuras versiones.
    
    Uso potencial:
    - Logging detallado de lecturas con timestamps
    - Auditoría de eventos del sistema de riego
    - Análisis histórico de condiciones ambientales
    - Debugging y troubleshooting
    
    Attributes:
        tipo_sensor: Tipo de sensor que generó el evento (TEMPERATURA o HUMEDAD).
        valor: Valor medido por el sensor (°C para temperatura, % para humedad).
        timestamp: Momento exacto en que se realizó la lectura.
        unidad: Unidad de medida del valor ("°C" o "%").

    """
    tipo_sensor: TipoSensor
    valor: float
    timestamp: datetime
    unidad: str

    def __str__(self) -> str:
        """
        Representación en cadena legible del evento.
        
        Returns:
            Cadena formateada con tipo, valor, unidad y timestamp.

        """
        return (f"[{self.tipo_sensor.name}] {self.valor}{self.unidad} - "
                f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    def es_temperatura(self) -> bool:
        """
        Verifica si el evento proviene de un sensor de temperatura.
        
        Returns:
            True si es evento de temperatura, False en caso contrario.

        """
        return self.tipo_sensor == TipoSensor.TEMPERATURA

    def es_humedad(self) -> bool:
        """
        Verifica si el evento proviene de un sensor de humedad.
        
        Returns:
            True si es evento de humedad, False en caso contrario.

        """
        return self.tipo_sensor == TipoSensor.HUMEDAD