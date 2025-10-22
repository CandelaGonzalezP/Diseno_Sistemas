from dataclasses import dataclass
from datetime import date

@dataclass
class AptoMedico:
    """
    Representa la certificación médica de un trabajador agrícola.
    
    Almacena la información sobre la aptitud médica laboral de un trabajador,
    incluyendo la fecha de emisión, estado de aptitud y observaciones médicas.
    
    Attributes:
        fecha_emision: Fecha en que se emitió el certificado médico.
        observaciones: Notas o comentarios del médico sobre el estado del trabajador.
        es_apto: Indica si el trabajador está apto para realizar tareas (True por defecto).
    """
    
    fecha_emision: date
    observaciones: str
    es_apto: bool = True
