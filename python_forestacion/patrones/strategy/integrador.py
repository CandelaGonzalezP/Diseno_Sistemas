"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ================================================================================

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from ...entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """
    Interfaz del patrón Strategy para algoritmos de absorción de agua en cultivos.
    
    Define el contrato que deben cumplir todas las estrategias de cálculo de absorción
    de agua. Permite intercambiar algoritmos de absorción en tiempo de ejecución sin
    modificar el código cliente (servicios de cultivos).
    
    El sistema implementa dos estrategias concretas:
    - AbsorcionSeasonalStrategy: Para árboles (Pino, Olivo) con absorción variable
      según estación (5L verano, 2L invierno)
    - AbsorcionConstanteStrategy: Para hortalizas (Lechuga, Zanahoria) con absorción
      fija (1-2L independiente de temporada)
    
    Este patrón cumple con:
    - Open/Closed Principle: Nuevas estrategias se agregan sin modificar existentes
    - Dependency Inversion: Servicios dependen de abstracción, no implementaciones
    - Strategy Pattern: Algoritmos encapsulados e intercambiables
    
    """
    
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        cultivo: Cultivo
    ) -> int:
        """
        Método abstracto que calcula la cantidad de agua absorbida por un cultivo.
        
        Las implementaciones concretas deben definir el algoritmo específico para
        calcular los litros de agua que el cultivo absorbe durante un riego.
        
        El método recibe la fecha del riego para permitir cálculos estacionales,
        y la instancia del cultivo para acceder a sus características si fuera necesario.
        
        Args:
            fecha: Fecha del riego, puede usarse para cálculos estacionales.
            cultivo: Instancia del cultivo que absorberá agua.
        
        Returns:
            Cantidad de litros de agua absorbidos por el cultivo (entero positivo).
        
        """
        pass

