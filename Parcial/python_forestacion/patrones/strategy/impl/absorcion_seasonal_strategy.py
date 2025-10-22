from datetime import date
from ..absorcion_agua_strategy import AbsorcionAguaStrategy
from ....entidades.cultivos.cultivo import Cultivo
from ....constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua estacional para cultivos arbóreos.
    
    Implementa el patrón Strategy para calcular la absorción de agua de árboles
    que tienen requerimientos hídricos variables según la estación del año.
    
    Los árboles (Pino y Olivo) absorben más agua durante el verano (marzo-agosto)
    debido a mayor evapotranspiración y crecimiento activo, mientras que en invierno
    (septiembre-febrero) su consumo es menor por menor actividad metabólica.
    
    Esta estrategia utiliza constantes centralizadas del sistema para definir:
    - Meses de verano: marzo (3) a agosto (8)
    - Absorción verano: 5 litros
    - Absorción invierno: 2 litros
    
    Attributes:
        Ninguno (utiliza constantes del sistema).

    """
 
    def calcular_absorcion(self, fecha: date, cultivo: Cultivo) -> int:
        """
        Calcula la absorción de agua según la estación del año.
        
        Evalúa el mes de la fecha proporcionada y retorna la cantidad de litros
        correspondiente a la estación:
        - Verano (marzo a agosto): ABSORCION_SEASONAL_VERANO (5L)
        - Invierno (septiembre a febrero): ABSORCION_SEASONAL_INVIERNO (2L)
        
        Esta implementación permite que árboles como Pino y Olivo ajusten
        automáticamente su consumo hídrico según la temporada.
        
        Args:
            fecha: Fecha del riego, utilizada para determinar la estación.
            cultivo: Instancia del cultivo a regar (no utilizada, incluida por interfaz).
        
        Returns:
            Cantidad de litros de agua absorbidos según la estación.
            - 5 litros si es verano (marzo-agosto)
            - 2 litros si es invierno (septiembre-febrero)
        
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO