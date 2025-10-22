from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enumeración de los tipos de aceitunas disponibles para olivos.
    
    Define las variedades de aceitunas que pueden producir los olivos
    en el sistema de gestión forestal.
    
    Attributes:
        ARBEQUINA: Variedad de aceituna arbequina, originaria de Cataluña.
        PICUAL: Variedad de aceituna picual, típica de Jaén.
        MANZANILLA: Variedad de aceituna manzanilla, común en Andalucía.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()