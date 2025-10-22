"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ================================================================================

from datetime import date
from ..absorcion_agua_strategy import AbsorcionAguaStrategy
from ....entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua constante para cultivos hortícolas.
    
    Implementa el patrón Strategy para calcular la absorción de agua de cultivos
    que mantienen un consumo hídrico constante independientemente de la estación
    del año o condiciones ambientales.
    
    Esta estrategia es utilizada por hortalizas como Lechuga (1L) y Zanahoria (2L),
    que requieren riego uniforme durante todo su ciclo de crecimiento.
    
    En el sistema, esta estrategia se inyecta en los servicios de cultivos hortícolas
    durante su inicialización, cumpliendo con el principio de Dependency Inversion.
    
    Attributes:
        _cantidad: Cantidad fija de litros de agua que el cultivo absorbe por riego.

    """

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia con una cantidad fija de absorción.
        
        Args:
            cantidad_constante: Cantidad de litros que el cultivo absorbe por riego.
                               Debe ser un valor positivo.

        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, cultivo: Cultivo) -> int:
        """
        Calcula la absorción de agua retornando siempre la cantidad constante.
        
        A diferencia de AbsorcionSeasonalStrategy, este método ignora la fecha
        y las condiciones ambientales, retornando siempre el mismo valor definido
        en el constructor.
        
        Args:
            fecha: Fecha del riego (no utilizada en esta estrategia).
            cultivo: Instancia del cultivo a regar (no utilizada en esta estrategia).
        
        Returns:
            Cantidad constante de litros de agua absorbidos.
        """
        return self._cantidad

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ================================================================================

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

