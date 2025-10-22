from .cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.arbol import Arbol

class ArbolService(CultivoService):
    """
    Servicio base para operaciones relacionadas con cultivos arbóreos.
    
    Define comportamiento común para todos los árboles del sistema (Pino, Olivo),
    proporcionando implementaciones genéricas de plantación y cosecha que pueden
    ser especializadas por servicios hijos.
    
    Hereda de CultivoService e implementa la interfaz abstracta con lógica
    específica para árboles. Los servicios concretos (PinoService, OlivoService)
    pueden sobrescribir estos métodos para agregar comportamiento especializado.
    
    Este diseño implementa el patrón Template Method, donde la clase base define
    el esqueleto de las operaciones y las subclases refinan pasos específicos.
    
    Características de los árboles:
    - Ciclo de vida largo (varios años)
    - Requieren mayor superficie que hortalizas
    - Crecen en altura con cada riego
    - Absorción de agua estacional
    
    Attributes:
        Ninguno específico - hereda de CultivoService.

    """
    
    def plantar(self, arbol: Arbol):
        """
        Define la lógica genérica para plantar un árbol.
        
        Implementa el método abstracto de CultivoService con comportamiento
        común a todos los árboles. Registra la operación de plantación mostrando
        el tipo de árbol y su edad.
        
        Los servicios especializados (PinoService, OlivoService) heredan este
        comportamiento o pueden sobrescribirlo para agregar lógica adicional.
        
        Args:
            arbol: Instancia de Arbol a plantar (Pino u Olivo).

        """
        print(f"SERVICIO: Plantando el árbol '{arbol.get_tipo()}' de {arbol.anios} años.")

    def cosechar(self, arbol: Arbol):
        """
        Define la lógica genérica para cosechar un árbol.
        
        Implementa el método abstracto de CultivoService con comportamiento
        básico de cosecha. Los servicios especializados típicamente sobrescriben
        este método para especificar qué se cosecha (madera de pino vs aceitunas
        de olivo).
        
        Args:
            arbol: Instancia de Arbol a cosechar (Pino u Olivo).
        
        """
        print(f"SERVICIO: Cosechando el árbol '{arbol.get_tipo()}'.")