from .arbol_service import ArbolService
from ...entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """
    Servicio especializado para operaciones sobre cultivos de Pino.
    
    Hereda de ArbolService e implementa lógica específica para pinos,
    árboles maderables con ciclo de vida largo y requerimientos de riego
    estacional para producción forestal.
    
    Características del Pino:
    - Árbol maderable de larga vida (20-40 años hasta corte)
    - Superficie: 2.0 m² por árbol
    - Absorción estacional: 5L verano, 2L invierno
    - Variedades: Paraná, Elliott, Taeda, etc.
    - Crecimiento: +0.10m por riego (más rápido que olivo)
    - Altura inicial: 1.0m
    
    El servicio hereda el método plantar() de ArbolService pero especializa
    la cosecha para reflejar que se extrae madera, el producto final de
    la forestación de pinos.
    
    Attributes:
        Ninguno específico - hereda de ArbolService.
    
    """

    def cosechar(self, pino: Pino):
        """
        Especializa la lógica de cosecha para pinos.
        
        Sobrescribe el método genérico de ArbolService para especificar que
        se está cosechando madera del pino de la variedad específica.
        
        En un sistema real, este método podría incluir:
        - Cálculo de volumen maderable en m³
        - Clasificación de calidad de madera
        - Estimación de tablones o pulpa
        - Registro de edad del árbol al corte
        - Cálculo de valor comercial
        
        Args:
            pino: Instancia de Pino a cosechar.
        
        """
        print(f"SERVICIO: Cosechando madera del Pino variedad '{pino.variedad}'.")