from .arbol import Arbol
from .tipo_aceituna import TipoAceituna
from ...constantes import SUPERFICIE_OLIVO_M2, CRECIMIENTO_OLIVO_POR_RIEGO_M

class Olivo(Arbol):
    """
    Representa un árbol de olivo con tipo de aceituna específico.
    
    El olivo es un árbol frutal que produce aceitunas y requiere
    cuidados específicos para su crecimiento.
    
    Attributes:
        _tipo_aceituna: Variedad de aceituna que produce el olivo.
    """

    def __init__(self, anios: int = 0, tipo_aceituna: TipoAceituna = TipoAceituna.ARBEQUINA):
        """
        Inicializa un nuevo olivo con sus características.
        
        Args:
            anios: Edad inicial del olivo en años. Por defecto 0.
            tipo_aceituna: Variedad de aceituna del olivo. Por defecto ARBEQUINA.
        """
        super().__init__(anios=anios, agua_inicial=5.0, altura_inicial=0.5)
        self._tipo_aceituna = tipo_aceituna
        self._metros_cuadrados_requeridos = SUPERFICIE_OLIVO_M2

    @property
    def tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna que produce el olivo.
        
        Returns:
            Enumeración TipoAceituna correspondiente.
        """
        return self._tipo_aceituna

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento del olivo al recibir agua.
        
        Incrementa tanto el agua absorbida como la altura del árbol
        según la constante de crecimiento definida para olivos.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        self._litros_agua_absorbidos += litros_agua
        self._altura_metros += CRECIMIENTO_OLIVO_POR_RIEGO_M
        print(f"El Olivo de aceituna '{self.tipo_aceituna.name}' creció a {self.altura_metros:.2f}m.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Olivo".
        """
        return "Olivo"
