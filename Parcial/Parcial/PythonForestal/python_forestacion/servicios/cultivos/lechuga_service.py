from .cultivo_service import CultivoService
from ...entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """
    Servicio especializado para operaciones sobre cultivos de Lechuga.
    
    Implementa la interfaz CultivoService con lógica específica para lechugas,
    una hortaliza de hoja verde cultivada en invernadero con ciclo de crecimiento
    corto y requerimientos de riego constantes.
    
    Características de la Lechuga:
    - Cultivo en invernadero (invernadero=True)
    - Superficie reducida: 0.10 m² por planta
    - Absorción constante: 1 litro por riego
    - Variedades: Crespa, Mantecosa, Morada, etc.
    - Ciclo corto: 60-90 días desde plantación a cosecha
    
    Este servicio no maneja estrategias de absorción directamente - delega
    esa responsabilidad al CultivoServiceRegistry que aplica absorción constante.
    
    Attributes:
        Ninguno específico - implementa interfaz de CultivoService.
    
    """

    def plantar(self, lechuga: Lechuga):
        """
        Implementa la plantación específica de lechugas.
        
        Registra la operación de plantación mostrando el tipo de cultivo y
        la variedad específica de lechuga. En un sistema real, este método
        podría incluir:
        - Validación de condiciones de invernadero
        - Registro de fecha de plantación
        - Inicialización de cronograma de cosecha
        
        Args:
            lechuga: Instancia de Lechuga a plantar.
        
        """
        print(f"SERVICIO: Plantando la hortaliza Lechuga variedad '{lechuga.variedad}'.")

    def cosechar(self, lechuga: Lechuga):
        """
        Implementa la cosecha específica de lechugas.
        
        Registra la operación de cosecha de hojas, especificando la variedad.
        Las lechugas se cosechan extrayendo las hojas verdes comestibles,
        típicamente cuando alcanzan tamaño comercial.
        
        Args:
            lechuga: Instancia de Lechuga a cosechar.
        
        """
        print(f"SERVICIO: Cosechando hojas de Lechuga variedad '{lechuga.variedad}'.")