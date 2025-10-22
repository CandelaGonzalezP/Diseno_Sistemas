"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\arbol_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\cultivo_service.py
# ================================================================================

from abc import ABC, abstractmethod
from ...entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """
    Clase base abstracta para todos los servicios de cultivos del sistema.
    
    Define el contrato que deben cumplir todos los servicios de cultivos,
    estableciendo las operaciones fundamentales de plantación y cosecha.
    
    Esta clase implementa el patrón Template Method al nivel de interfaz,
    forzando a las subclases a implementar operaciones específicas mientras
    mantiene una estructura consistente en toda la jerarquía de servicios.
    
    """
    
    @abstractmethod
    def plantar(self, cultivo: Cultivo):
        """
        Método abstracto para plantar un cultivo.
        
        Las subclases deben implementar la lógica específica de plantación
        para su tipo de cultivo, incluyendo validaciones, registro de eventos,
        y cualquier inicialización necesaria.
        
        Args:
            cultivo: Instancia del cultivo a plantar.

        """
        pass

    @abstractmethod
    def cosechar(self, cultivo: Cultivo):
        """
        Método abstracto para cosechar un cultivo.
        
        Las subclases deben implementar la lógica específica de cosecha
        para su tipo de cultivo, especificando qué se extrae (madera, aceitunas,
        hojas, raíces) y cualquier procesamiento post-cosecha.
        
        Args:
            cultivo: Instancia del cultivo a cosechar.

        """
        pass

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ================================================================================

from threading import Lock
from datetime import date

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_CONSTANTE_HORTALIZAS
)

class CultivoServiceRegistry:
    """
    Registro centralizado implementando patrones Singleton y Registry.
    
    Proporciona punto único de acceso para operaciones sobre cultivos mediante
    dispatch polimórfico, eliminando cascadas de isinstance().
    
    Operaciones soportadas:
    - Absorción de agua (estacional para árboles, constante para hortalizas)
    - Visualización de datos específicos por tipo
    
    Singleton thread-safe con double-checked locking.
    
    Attributes:
        _instance: Instancia única compartida.
        _lock: Lock para thread-safety.
        _absorber_agua_handlers: Handlers de absorción por tipo.
        _mostrar_datos_handlers: Handlers de visualización por tipo.
        _initialized: Flag de inicialización única.
    """
    
    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Garantiza Singleton thread-safe mediante double-checked locking.
        
        Returns:
            La instancia única de CultivoServiceRegistry.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Inicializa handlers solo en la primera instanciación.
        
        Registra handlers de absorción y visualización para cada tipo de cultivo.
        El flag _initialized evita reinicialización en llamadas posteriores.
        """
        if hasattr(self, '_initialized'):
            return
        
        print("INFO: Inicializando Registry y handlers.")
        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_arbol_seasonal,
            Olivo: self._absorber_agua_arbol_seasonal,
            Lechuga: self._absorber_agua_hortaliza_constante,
            Zanahoria: self._absorber_agua_hortaliza_constante
        }
        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }
        self._initialized = True

    def _absorber_agua_arbol_seasonal(self, cultivo: Cultivo, fecha: date) -> int:
        """
        Handler de absorción estacional para árboles.
        
        Args:
            cultivo: Árbol a evaluar.
            fecha: Fecha para determinar estación.
        
        Returns:
            5L si verano (junio-agosto), 2L si invierno.
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO

    def _absorber_agua_hortaliza_constante(self, cultivo: Cultivo, fecha: date) -> int:
        """
        Handler de absorción constante para hortalizas.
        
        Args:
            cultivo: Hortaliza a evaluar.
            fecha: No utilizada en absorción constante.
        
        Returns:
            Cantidad fija definida en constantes.
        """
        return ABSORCION_CONSTANTE_HORTALIZAS

    def _mostrar_datos_pino(self, pino: Pino):
        """
        Muestra datos específicos de Pino.
        
        Args:
            pino: Instancia a visualizar.
        """
        print(f"Cultivo: {pino.get_tipo()}")
        print(f"Superficie: {pino.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {pino.litros_agua_absorbidos} L")
        print(f"Altura: {pino.altura_metros:.2f} m")
        print(f"Variedad: {pino.variedad}")

    def _mostrar_datos_olivo(self, olivo: Olivo):
        """
        Muestra datos específicos de Olivo.
        
        Args:
            olivo: Instancia a visualizar.
        """
        print(f"Cultivo: {olivo.get_tipo()}")
        print(f"Superficie: {olivo.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {olivo.litros_agua_absorbidos} L")
        print(f"Altura: {olivo.altura_metros:.2f} m")
        print(f"Tipo de aceituna: {olivo.tipo_aceituna.name}")

    def _mostrar_datos_lechuga(self, lechuga: Lechuga):
        """
        Muestra datos específicos de Lechuga.
        
        Args:
            lechuga: Instancia a visualizar.
        """
        print(f"Cultivo: {lechuga.get_tipo()}")
        print(f"Superficie: {lechuga.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {lechuga.litros_agua_absorbidos} L")
        print(f"Variedad: {lechuga.variedad}")
        print(f"Invernadero: True")

    def _mostrar_datos_zanahoria(self, zanahoria: Zanahoria):
        """
        Muestra datos específicos de Zanahoria.
        
        Args:
            zanahoria: Instancia a visualizar.
        """
        print(f"Cultivo: {zanahoria.get_tipo()}")
        print(f"Superficie: {zanahoria.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {zanahoria.litros_agua_absorbidos} L")
        print(f"Es baby carrot: {zanahoria.es_baby}")

    def absorber_agua(self, cultivo: Cultivo, fecha_actual: date) -> int:
        """
        Despacha absorción al handler correcto mediante Registry.
        
        Args:
            cultivo: Cultivo que absorberá agua.
            fecha_actual: Fecha para cálculos estacionales.
        
        Returns:
            Litros absorbidos según tipo y estrategia.
        
        Raises:
            TypeError: Si no existe handler para el tipo.
        """
        tipo_cultivo = type(cultivo)
        handler = self._absorber_agua_handlers.get(tipo_cultivo)
        if not handler:
            raise TypeError(f"No hay un handler de absorción de agua para '{tipo_cultivo.__name__}'")
        return handler(cultivo, fecha_actual)

    def mostrar_datos(self, cultivo: Cultivo):
        """
        Despacha visualización al handler correcto mediante Registry.
        
        Args:
            cultivo: Cultivo a visualizar.
        
        Raises:
            TypeError: Si no existe handler para el tipo.
        """
        print("-" * 20)
        tipo_cultivo = type(cultivo)
        handler = self._mostrar_datos_handlers.get(tipo_cultivo)
        if not handler:
            raise TypeError(f"No hay un handler para mostrar datos de '{tipo_cultivo.__name__}'")
        handler(cultivo)

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\lechuga_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\olivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\pino_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\zanahoria_service.py
# ================================================================================

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

