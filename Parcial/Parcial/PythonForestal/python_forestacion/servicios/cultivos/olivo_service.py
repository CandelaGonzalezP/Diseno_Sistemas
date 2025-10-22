from .arbol_service import ArbolService
from ...entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """
    Servicio especializado para operaciones sobre cultivos de Olivo.
    
    Hereda de ArbolService e implementa lógica específica para olivos,
    árboles frutales cultivados por sus aceitunas con ciclo de vida perenne
    y requerimientos de riego estacional.
    
    Características del Olivo:
    - Árbol frutal de larga vida (décadas)
    - Superficie: 3.0 m² por árbol
    - Absorción estacional: 5L verano, 2L invierno
    - Tipos de aceituna: Arbequina, Picual, Manzanilla
    - Crecimiento: +0.01m por riego
    - Altura inicial: 0.5m
    
    El servicio hereda el método plantar() de ArbolService pero especializa
    la cosecha para reflejar que se extraen aceitunas, no madera.
    
    Attributes:
        Ninguno específico - hereda de ArbolService.
    
    """

    def cosechar(self, olivo: Olivo):
        """
        Especializa la lógica de cosecha para olivos.
        
        Sobrescribe el método genérico de ArbolService para especificar que
        se están cosechando aceitunas del tipo específico del olivo.
        
        En un sistema real, este método podría incluir:
        - Cálculo de rendimiento en kg de aceitunas
        - Clasificación por calidad (mesa vs aceite)
        - Registro de fecha de cosecha
        - Estimación de producción de aceite
        
        Args:
            olivo: Instancia de Olivo a cosechar.
        
        """
        print(f"SERVICIO: Cosechando aceitunas '{olivo.tipo_aceituna.name}' del Olivo.")