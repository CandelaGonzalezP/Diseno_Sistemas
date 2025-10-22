from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto

class EstadoTarea(Enum):
    """
    Enumeración de los estados posibles de una tarea agrícola.
    
    Define los estados del ciclo de vida de una tarea asignada a un trabajador.
    
    Attributes:
        PENDIENTE: La tarea está asignada pero aún no se ha ejecutado.
        COMPLETADA: La tarea ha sido ejecutada exitosamente.
    """
    PENDIENTE = auto()
    COMPLETADA = auto()

@dataclass
class Tarea:
    """
    Representa una tarea agrícola asignada a un trabajador.
    
    Define las actividades que deben realizar los trabajadores en la plantación,
    con su identificación, descripción, fecha programada y estado de ejecución.
    
    Attributes:
        id_tarea: Identificador único de la tarea.
        descripcion: Descripción detallada de la actividad a realizar
                    (ej. "Desmalezar", "Abonar", "Marcar surcos").
        fecha_programada: Fecha en que está programada la ejecución de la tarea.
        estado: Estado actual de la tarea (PENDIENTE por defecto).
    """
    id_tarea: int
    descripcion: str
    fecha_programada: date
    estado: EstadoTarea = field(default=EstadoTarea.PENDIENTE)
