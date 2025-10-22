from .cultivo_service import CultivoService
from ...entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """
    Servicio especializado para operaciones sobre cultivos de Zanahoria.
    
    Implementa la interfaz CultivoService con lógica específica para zanahorias,
    una hortaliza de raíz cultivada a campo abierto con dos variantes principales:
    zanahoria regular y baby carrot.
    
    Características de la Zanahoria:
    - Cultivo a campo abierto (invernadero=False)
    - Superficie: 0.15 m² por planta
    - Absorción constante: 2 litros por riego
    - Agua inicial: 0L (sin reserva inicial)
    - Tipos: Regular o Baby Carrot
    - Ciclo: 70-120 días según variedad
    
    El servicio adapta sus mensajes según el tipo de zanahoria (baby o regular),
    proporcionando trazabilidad específica para cada variante.
    
    Attributes:
        Ninguno específico - implementa interfaz de CultivoService.
    
    """

    def plantar(self, zanahoria: Zanahoria):
        """
        Implementa la plantación específica de zanahorias.
        
        Registra la operación de plantación distinguiendo entre zanahoria regular
        y baby carrot. En un sistema real, este método podría incluir:
        - Validación de profundidad de suelo
        - Espaciado según tipo (baby carrots más densas)
        - Registro de fecha de plantación
        - Inicialización de cronograma de cosecha
        
        Args:
            zanahoria: Instancia de Zanahoria a plantar.
    
        """
        tipo_zanahoria = "Baby" if zanahoria.es_baby else "Normal"
        print(f"SERVICIO: Plantando la hortaliza Zanahoria de tipo '{tipo_zanahoria}'.")

    def cosechar(self, zanahoria: Zanahoria):
        """
        Implementa la cosecha específica de zanahorias.
        
        Registra la operación de extracción de raíces distinguiendo entre
        zanahoria regular y baby carrot. Las zanahorias se cosechan extrayendo
        la raíz completa del suelo cuando alcanzan el tamaño comercial.
        
        Baby carrots típicamente se cosechan más temprano (70-80 días) mientras
        que las regulares necesitan más tiempo (100-120 días) para alcanzar
        tamaño completo.
        
        Args:
            zanahoria: Instancia de Zanahoria a cosechar.
        
        """
        tipo_zanahoria = "Baby" if zanahoria.es_baby else "Normal"
        print(f"SERVICIO: Extrayendo Zanahorias de tipo '{tipo_zanahoria}'.")