"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\
Fecha de generacion: 2025-10-22 08:32:43
Total de archivos integrados: 68
Total de directorios procesados: 22
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#   3. main.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades\personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades\terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones\factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones\observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones\observer\eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones\singleton
#   38. __init__.py
#
# DIRECTORIO: patrones\strategy
#   39. __init__.py
#   40. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   41. __init__.py
#   42. absorcion_constante_strategy.py
#   43. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   44. __init__.py
#
# DIRECTORIO: riego\control
#   45. __init__.py
#   46. control_riego_task.py
#
# DIRECTORIO: riego\sensores
#   47. __init__.py
#   48. humedad_reader_task.py
#   49. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   50. __init__.py
#
# DIRECTORIO: servicios\cultivos
#   51. __init__.py
#   52. arbol_service.py
#   53. cultivo_service.py
#   54. cultivo_service_registry.py
#   55. lechuga_service.py
#   56. olivo_service.py
#   57. pino_service.py
#   58. zanahoria_service.py
#
# DIRECTORIO: servicios\negocio
#   59. __init__.py
#   60. fincas_service.py
#   61. paquete.py
#
# DIRECTORIO: servicios\personal
#   62. __init__.py
#   63. trabajador_service.py
#
# DIRECTORIO: servicios\terrenos
#   64. __init__.py
#   65. plantacion_service.py
#   66. registro_forestal_service.py
#   67. tierra_service.py
#
# DIRECTORIO: tests
#   68. tests_casos_especificos.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/68: __init__.py
# Directorio: .
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/68: constantes.py
# Directorio: .
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\constantes.py
# ==============================================================================

# ==============================================================================
# ESTRATEGIA SEASONAL
# ==============================================================================
MES_INICIO_VERANO = 6
MES_FIN_VERANO = 8
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2

# ==============================================================================
# CARACTERÍSTICAS DE CULTIVOS 
# ==============================================================================
SUPERFICIE_PINO_M2 = 10.0
CRECIMIENTO_PINO_POR_RIEGO_M = 0.10
SUPERFICIE_OLIVO_M2 = 15.0
CRECIMIENTO_OLIVO_POR_RIEGO_M = 0.01
SUPERFICIE_LECHUGA_M2 = 0.5
SUPERFICIE_ZANAHORIA_M2 = 0.3
ABSORCION_CONSTANTE_HORTALIZAS = 2

# ==============================================================================
# SISTEMA DE RIEGO 
# ==============================================================================
TEMP_MIN_RIEGO = 8.0
TEMP_MAX_RIEGO = 15.0
HUMEDAD_MAX_RIEGO = 50.0
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5

SENSOR_TEMP_MIN = -25.0
SENSOR_TEMP_MAX = 50.0
SENSOR_HUMEDAD_MIN = 0.0
SENSOR_HUMEDAD_MAX = 100.0

THREAD_JOIN_TIMEOUT = 2.0

# ==============================================================================
# PERSISTENCIA 
# ==============================================================================
DIRECTORIO_DATOS_DEFAULT = "data""""
Constantes centralizadas del sistema de gestión forestal.

Agrupa todos los valores mágicos del sistema en un único archivo para facilitar
mantenimiento y configuración. Organizado por categorías funcionales.

Principio DRY (Don't Repeat Yourself): Ningún valor debe estar hardcodeado
en el código - todos deben referenciarse desde este módulo.
"""

# ==============================================================================
# ESTRATEGIA SEASONAL
# ==============================================================================
MES_INICIO_VERANO = 6
"""Mes de inicio del verano en el hemisferio sur (junio)."""

MES_FIN_VERANO = 8
"""Mes de fin del verano en el hemisferio sur (agosto)."""

ABSORCION_SEASONAL_VERANO = 5
"""Litros absorbidos por árboles durante el verano."""

ABSORCION_SEASONAL_INVIERNO = 2
"""Litros absorbidos por árboles durante el invierno."""

# ==============================================================================
# CARACTERÍSTICAS DE CULTIVOS 
# ==============================================================================
SUPERFICIE_PINO_M2 = 10.0
"""Superficie requerida por cada pino en metros cuadrados."""

CRECIMIENTO_PINO_POR_RIEGO_M = 0.10
"""Incremento de altura del pino por cada riego en metros."""

SUPERFICIE_OLIVO_M2 = 15.0
"""Superficie requerida por cada olivo en metros cuadrados."""

CRECIMIENTO_OLIVO_POR_RIEGO_M = 0.01
"""Incremento de altura del olivo por cada riego en metros."""

SUPERFICIE_LECHUGA_M2 = 0.5
"""Superficie requerida por cada lechuga en metros cuadrados."""

SUPERFICIE_ZANAHORIA_M2 = 0.3
"""Superficie requerida por cada zanahoria en metros cuadrados."""

ABSORCION_CONSTANTE_HORTALIZAS = 2
"""Litros absorbidos por hortalizas en cada riego (valor constante)."""

# ==============================================================================
# SISTEMA DE RIEGO 
# ==============================================================================
TEMP_MIN_RIEGO = 8.0
"""Temperatura mínima en °C para activar riego automático."""

TEMP_MAX_RIEGO = 15.0
"""Temperatura máxima en °C para activar riego automático."""

HUMEDAD_MAX_RIEGO = 50.0
"""Humedad máxima en % para activar riego automático."""

INTERVALO_SENSOR_TEMPERATURA = 2.0
"""Intervalo de lectura del sensor de temperatura en segundos."""

INTERVALO_SENSOR_HUMEDAD = 3.0
"""Intervalo de lectura del sensor de humedad en segundos."""

INTERVALO_CONTROL_RIEGO = 2.5
"""Intervalo de evaluación del controlador de riego en segundos."""

# --- RANGOS DE VALORES DE SENSORES ---
SENSOR_TEMP_MIN = -25.0
"""Temperatura mínima simulada por el sensor en °C."""

SENSOR_TEMP_MAX = 50.0
"""Temperatura máxima simulada por el sensor en °C."""

SENSOR_HUMEDAD_MIN = 0.0
"""Humedad mínima simulada por el sensor en %."""

SENSOR_HUMEDAD_MAX = 100.0
"""Humedad máxima simulada por el sensor en %."""

THREAD_JOIN_TIMEOUT = 2.0
"""Timeout para esperar finalización de threads en segundos."""

# ==============================================================================
# PERSISTENCIA 
# ==============================================================================
DIRECTORIO_DATOS_DEFAULT = "data"
"""Directorio por defecto para almacenar archivos .dat de registros forestales."""

# ==============================================================================
# ARCHIVO 3/68: main.py
# Directorio: .
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\main.py
# ==============================================================================

import sys
import os
import time
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.entidades.personal.trabajador import Trabajador, AptoMedico, Tarea

def run():
    """Función principal que ejecuta la simulación completa."""

    # ======================================================================
    # ENCABEZADO DE LA APLICACIÓN
    # ======================================================================
    print("=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)

    # ======================================================================
    # PATRON SINGLETON Y REGISTRY: Inicializando servicios
    # ======================================================================
    print("\n" + "-" * 70)
    print("  PATRON SINGLETON Y REGISTRY: Inicializando servicios")
    print("-" * 70)
    registry = CultivoServiceRegistry()
    registry2 = CultivoServiceRegistry()
    if registry is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry.")
    else:
        print("[FAIL] Las instancias del Registry son diferentes.")

    fincas_service = FincasService()
    registro_perez = fincas_service.crear_registro_completo(
        propietario="Juan Perez",
        avaluo=50309233.55,
        padron_tierra="01-12345",
        superficie_tierra=100.0,  
        domicilio_tierra="Agrelo, Luján de Cuyo, Mendoza",
        nombre_plantacion="Finca Los Andes",
        agua_litros=5000.0
    )
    plantacion = registro_perez.plantacion

    # ======================================================================
    # PATRON FACTORY METHOD: Plantando cultivos
    # ======================================================================
    print("\n" + "-" * 70)
    print("  PATRON FACTORY METHOD: Plantando cultivos")
    print("-" * 70)
    plantacion_service = PlantacionService()
    plantacion_service.plantar_cultivos_en_lote(plantacion, "Pino", 5)
    plantacion_service.plantar_cultivos_en_lote(plantacion, "Lechuga", 10)

    # ======================================================================
    # PATRON STRATEGY Y REGISTRY: Riego de cultivos
    # ======================================================================
    print("\n" + "-" * 70)
    print("  PATRON STRATEGY Y REGISTRY: Riego de cultivos")
    print("-" * 70)
    plantacion_service.regar_plantacion(plantacion)

    # ======================================================================
    # MANEJO DE EXCEPCIONES: Intentando plantar en exceso
    # ======================================================================
    print("\n" + "-" * 70)
    print("  MANEJO DE EXCEPCIONES: Intentando plantar en exceso")
    print("-" * 70)
    try:
        plantacion_service.plantar_cultivos_en_lote(plantacion, "Olivo", 10)
    except SuperficieInsuficienteException as e:
        print(f"[OK] Excepción capturada correctamente: {e.get_user_message()}")
        print(f"     Requerida: {e.get_superficie_requerida():.2f} m², Disponible: {e.get_superficie_disponible():.2f} m²")

    # ======================================================================
    # GESTIÓN DE PERSONAL: Asignando y ejecutando tareas
    # ======================================================================
    print("\n" + "-" * 70)
    print("  GESTIÓN DE PERSONAL: Asignando y ejecutando tareas")
    print("-" * 70)
    apto_ok = AptoMedico(fecha_emision=date(2025, 10, 21), observaciones="Sin problemas")
    trabajador_gomez = Trabajador(dni=25123456, nombre="Carlos Gomez", apto_medico=apto_ok)
    plantacion.asignar_trabajador(trabajador_gomez)

    tarea1 = Tarea(id_tarea=101, descripcion="Revisar sistema de riego", fecha_programada=date.today())
    tarea2 = Tarea(id_tarea=102, descripcion="Podar Olivos", fecha_programada=date.today())
    trabajador_gomez.asignar_tarea(tarea1)
    trabajador_gomez.asignar_tarea(tarea2)
    trabajador_gomez.ejecutar_tareas()

    # ======================================================================
    # PATRON OBSERVER: Sistema de riego automatizado
    # ======================================================================
    print("\n" + "-" * 70)
    print("  PATRON OBSERVER: Iniciando sistema de riego automatizado")
    print("-" * 70)
    sensor_temp = TemperaturaReaderTask()
    sensor_hum = HumedadReaderTask()
    control_riego = ControlRiegoTask(sensor_temp, sensor_hum, plantacion, plantacion_service)

    sensor_temp.daemon = True
    sensor_hum.daemon = True
    control_riego.daemon = True
    sensor_temp.start()
    sensor_hum.start()
    control_riego.start()

    print("\nSistema de monitoreo funcionando en segundo plano durante 10 segundos...")
    time.sleep(10)

    sensor_temp.detener()
    sensor_hum.detener()
    control_riego.detener()
    print("Sistema de monitoreo detenido.")

    # ======================================================================
    # COSECHA Y EMPAQUETADO
    # ======================================================================
    print("\n" + "-" * 70)
    print("  COSECHA Y EMPAQUETADO")
    print("-" * 70)
    plantacion_service.cosechar_plantacion(plantacion)

    # ======================================================================
    # PERSISTENCIA DE DATOS
    # ======================================================================
    print("\n" + "-" * 70)
    print("  PERSISTENCIA: Guardando y cargando el registro forestal")
    print("-" * 70)
    registro_service = RegistroForestalService(directorio_datos="data")
    try:
        registro_service.persistir(registro_perez)
        registro_cargado = RegistroForestalService.leer_registro("Juan Perez")
        if registro_cargado:
            print(f"[OK] Registro cargado para: {registro_cargado.propietario}")
            registro_service.mostrar_datos(registro_cargado)
    except PersistenciaException as e:
        print(f"[FAIL] Ocurrió un error de persistencia: {e}")

    # ======================================================================
    # RESUMEN FINAL
    # ======================================================================
    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua (usado en Registry)")
    print("  [OK] REGISTRY    - Despacho polimorfico de operaciones")
    print("=" * 70)

if __name__ == "__main__":
    run()


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/68: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/68: __init__.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/68: arbol.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\arbol.py
# ==============================================================================

from abc import abstractmethod
from .cultivo import Cultivo

class Arbol(Cultivo):
    """
    Clase base abstracta para cultivos de tipo árbol.
    
    Extiende la funcionalidad de Cultivo añadiendo características específicas
    de árboles como edad y altura.
    
    Attributes:
        _anios: Edad del árbol en años.
        _altura_metros: Altura actual del árbol en metros.
    """

    def __init__(self, anios: int = 0, agua_inicial: float = 0.0, altura_inicial: float = 0.0):
        """
        Inicializa un nuevo árbol con sus características.
        
        Args:
            anios: Edad inicial del árbol en años. Por defecto 0.
            agua_inicial: Cantidad inicial de agua absorbida en litros. Por defecto 0.0.
            altura_inicial: Altura inicial del árbol en metros. Por defecto 0.0.
        """
        super().__init__(agua_inicial)
        self._anios = anios
        self._altura_metros = altura_inicial

    @property
    def anios(self) -> int:
        """
        Obtiene la edad del árbol.
        
        Returns:
            Edad en años.
        """
        return self._anios

    @property
    def altura_metros(self) -> float:
        """
        Obtiene la altura actual del árbol.
        
        Returns:
            Altura en metros.
        """
        return self._altura_metros

    @abstractmethod
    def crecer(self, litros_agua: float):
        """
        Define el comportamiento de crecimiento específico del árbol al ser regado.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
            
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        pass

# ==============================================================================
# ARCHIVO 7/68: cultivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

from abc import ABC, abstractmethod

class Cultivo(ABC):
    """
    Clase base abstracta que representa cualquier tipo de cultivo plantable.
    
    Define la interfaz común para todos los cultivos del sistema forestal,
    incluyendo árboles y hortalizas.
    
    Attributes:
        _litros_agua_absorbidos: Cantidad total de agua absorbida por el cultivo.
        _metros_cuadrados_requeridos: Superficie necesaria para plantar el cultivo.
    """

    def __init__(self, agua_inicial: float = 0.0):
        """
        Inicializa un nuevo cultivo con agua inicial.
        
        Args:
            agua_inicial: Cantidad inicial de agua absorbida en litros. Por defecto 0.0.
        """
        self._litros_agua_absorbidos = agua_inicial
        self._metros_cuadrados_requeridos = 0.0

    @property
    def litros_agua_absorbidos(self) -> float:
        """
        Obtiene la cantidad total de agua absorbida por el cultivo.
        
        Returns:
            Cantidad de agua en litros.
        """
        return self._litros_agua_absorbidos

    @property
    def metros_cuadrados_requeridos(self) -> float:
        """
        Obtiene la superficie requerida para plantar el cultivo.
        
        Returns:
            Superficie en metros cuadrados.
        """
        return self._metros_cuadrados_requeridos

    @abstractmethod
    def crecer(self, litros_agua: float):
        """
        Define el comportamiento de crecimiento del cultivo al ser regado.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
            
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        pass

    @abstractmethod
    def get_tipo(self) -> str:
        """
        Devuelve el nombre o tipo del cultivo.
        
        Returns:
            Nombre del tipo de cultivo como cadena de texto.
            
        Raises:
            NotImplementedError: Si la subclase no implementa este método.
        """
        pass


# ==============================================================================
# ARCHIVO 8/68: hortaliza.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\hortaliza.py
# ==============================================================================

from .cultivo import Cultivo

class Hortaliza(Cultivo):
    """
    Clase base para cultivos de tipo hortaliza.
    
    Extiende la funcionalidad de Cultivo para hortalizas, que tienen
    un comportamiento de crecimiento más simple que los árboles.
    """

    def __init__(self, agua_inicial: float = 0.0):
        """
        Inicializa una nueva hortaliza.
        
        Args:
            agua_inicial: Cantidad inicial de agua absorbida en litros. Por defecto 0.0.
        """
        super().__init__(agua_inicial)
    
    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento de la hortaliza absorbiendo agua.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        self._litros_agua_absorbidos += litros_agua


# ==============================================================================
# ARCHIVO 9/68: lechuga.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

from .hortaliza import Hortaliza
from ...constantes import SUPERFICIE_LECHUGA_M2

class Lechuga(Hortaliza):
    """
    Representa una hortaliza de tipo lechuga con variedad específica.
    
    La lechuga es una hortaliza de hoja verde que típicamente se cultiva
    en invernaderos y requiere riego constante.
    
    Attributes:
        _variedad: Tipo de lechuga (ej. Invernadero, Crespa, Mantecosa).
    """

    def __init__(self, variedad: str = "Invernadero"):
        """
        Inicializa una nueva lechuga con su variedad.
        
        Args:
            variedad: Tipo de lechuga a cultivar. Por defecto "Invernadero".
        """
        super().__init__(agua_inicial=1.0)
        self._variedad = variedad
        self._metros_cuadrados_requeridos = SUPERFICIE_LECHUGA_M2

    @property
    def variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.
        
        Returns:
            Nombre de la variedad como cadena de texto.
        """
        return self._variedad

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento de la lechuga al recibir agua.
        
        Incrementa el agua absorbida y muestra información del riego.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        super().crecer(litros_agua)
        print(f"La Lechuga variedad '{self.variedad}' absorbió {litros_agua}L de agua.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Lechuga".
        """
        return "Lechuga"


# ==============================================================================
# ARCHIVO 10/68: olivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 11/68: pino.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

from .arbol import Arbol
from ...constantes import SUPERFICIE_PINO_M2, CRECIMIENTO_PINO_POR_RIEGO_M

class Pino(Arbol):
    """
    Representa un árbol de pino con variedad específica.
    
    El pino es un árbol maderable que requiere superficie considerable
    y crece de manera constante con cada riego.
    
    Attributes:
        _variedad: Tipo de pino (ej. Paraná, Elliott, Taeda).
    """

    def __init__(self, anios: int = 0, variedad: str = "Parana"):
        """
        Inicializa un nuevo pino con sus características.
        
        Args:
            anios: Edad inicial del pino en años. Por defecto 0.
            variedad: Tipo de pino a plantar. Por defecto "Parana".
        """
        super().__init__(anios=anios, agua_inicial=2.0, altura_inicial=1.0)
        self._variedad = variedad
        self._metros_cuadrados_requeridos = SUPERFICIE_PINO_M2

    @property
    def variedad(self) -> str:
        """
        Obtiene la variedad del pino.
        
        Returns:
            Nombre de la variedad como cadena de texto.
        """
        return self._variedad

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento del pino al recibir agua.
        
        Incrementa tanto el agua absorbida como la altura del árbol
        según la constante de crecimiento definida.
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        self._litros_agua_absorbidos += litros_agua
        self._altura_metros += CRECIMIENTO_PINO_POR_RIEGO_M
        print(f"El Pino variedad '{self.variedad}' creció a {self.altura_metros:.2f}m.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Pino".
        """
        return "Pino"


# ==============================================================================
# ARCHIVO 12/68: tipo_aceituna.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ==============================================================================

from enum import Enum, auto

class TipoAceituna(Enum):
    """
    Enumeración de los tipos de aceitunas disponibles para olivos.
    
    Define las variedades de aceitunas que pueden producir los olivos
    en el sistema de gestión forestal.
    
    Attributes:
        ARBEQUINA: Variedad de aceituna arbequina, originaria de Cataluña.
        PICUAL: Variedad de aceituna picual, típica de Jaén.
        MANZANILLA: Variedad de aceituna manzanilla, común en Andalucía.
    """
    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()

# ==============================================================================
# ARCHIVO 13/68: zanahoria.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

from .hortaliza import Hortaliza
from ...constantes import SUPERFICIE_ZANAHORIA_M2

class Zanahoria(Hortaliza):
    """
    Representa una hortaliza de tipo zanahoria.
    
    La zanahoria puede ser de tipo normal o baby carrot, con diferentes
    características según su tipo.
    
    Attributes:
        _es_baby: Indica si es una zanahoria tipo baby carrot.
    """

    def __init__(self, es_baby: bool = False):
        """
        Inicializa una nueva zanahoria.
        
        Args:
            es_baby: Indica si es baby carrot (True) o normal (False). Por defecto False.
        """
        super().__init__(agua_inicial=0.0)
        self._es_baby = es_baby
        self._metros_cuadrados_requeridos = SUPERFICIE_ZANAHORIA_M2

    @property
    def es_baby(self) -> bool:
        """
        Verifica si la zanahoria es tipo baby carrot.
        
        Returns:
            True si es baby carrot, False si es normal.
        """
        return self._es_baby

    def crecer(self, litros_agua: float):
        """
        Implementa el crecimiento de la zanahoria al recibir agua.
        
        Incrementa el agua absorbida y muestra información según el tipo
        de zanahoria (baby o normal).
        
        Args:
            litros_agua: Cantidad de agua aplicada en litros.
        """
        super().crecer(litros_agua)
        tipo_zanahoria = "Baby" if self.es_baby else "Normal"
        print(f"La Zanahoria '{tipo_zanahoria}' absorbió {litros_agua}L de agua.")

    def get_tipo(self) -> str:
        """
        Devuelve el tipo de cultivo.
        
        Returns:
            La cadena "Zanahoria".
        """
        return "Zanahoria"



################################################################################
# DIRECTORIO: entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 14/68: __init__.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/68: apto_medico.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\apto_medico.py
# ==============================================================================

from dataclasses import dataclass
from datetime import date

@dataclass
class AptoMedico:
    """
    Representa la certificación médica de un trabajador agrícola.
    
    Almacena la información sobre la aptitud médica laboral de un trabajador,
    incluyendo la fecha de emisión, estado de aptitud y observaciones médicas.
    
    Attributes:
        fecha_emision: Fecha en que se emitió el certificado médico.
        observaciones: Notas o comentarios del médico sobre el estado del trabajador.
        es_apto: Indica si el trabajador está apto para realizar tareas (True por defecto).
    """
    
    fecha_emision: date
    observaciones: str
    es_apto: bool = True


# ==============================================================================
# ARCHIVO 16/68: herramienta.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\herramienta.py
# ==============================================================================

from dataclasses import dataclass

@dataclass
class Herramienta:
    """
    Representa una herramienta de trabajo agrícola.
    
    Define las herramientas que pueden ser asignadas a los trabajadores
    para la ejecución de sus tareas, incluyendo su identificación única,
    nombre y certificación de higiene y seguridad.
    
    Attributes:
        id_unico: Identificador único de la herramienta en el sistema.
        nombre: Nombre descriptivo de la herramienta (ej. "Pala", "Rastrillo").
        certificacion_hs: Indica si la herramienta cuenta con certificación
                         de higiene y seguridad vigente.
    """
 
    id_unico: int
    nombre: str
    certificacion_hs: bool

# ==============================================================================
# ARCHIVO 17/68: tarea.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\tarea.py
# ==============================================================================

from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto

class EstadoTarea(Enum):
    """
    Enumeración de los estados posibles de una tarea agrícola.
    
    Define los estados del ciclo de vida de una tarea asignada a un trabajador.
    
    Attributes:
        PENDIENTE: La tarea está asignada pero aún no se ha ejecutado.
        COMPLETADA: La tarea ha sido ejecutada exitosamente.
    """
    PENDIENTE = auto()
    COMPLETADA = auto()

@dataclass
class Tarea:
    """
    Representa una tarea agrícola asignada a un trabajador.
    
    Define las actividades que deben realizar los trabajadores en la plantación,
    con su identificación, descripción, fecha programada y estado de ejecución.
    
    Attributes:
        id_tarea: Identificador único de la tarea.
        descripcion: Descripción detallada de la actividad a realizar
                    (ej. "Desmalezar", "Abonar", "Marcar surcos").
        fecha_programada: Fecha en que está programada la ejecución de la tarea.
        estado: Estado actual de la tarea (PENDIENTE por defecto).
    """
    id_tarea: int
    descripcion: str
    fecha_programada: date
    estado: EstadoTarea = field(default=EstadoTarea.PENDIENTE)


# ==============================================================================
# ARCHIVO 18/68: trabajador.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\trabajador.py
# ==============================================================================

from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING
from .apto_medico import AptoMedico
from .tarea import Tarea, EstadoTarea
from .herramienta import Herramienta

if TYPE_CHECKING:
    from ..terrenos.plantacion import Plantacion

@dataclass
class Trabajador:
    """
    Representa a un trabajador agrícola con sus datos, certificaciones y tareas.
    
    Gestiona la información de los trabajadores del sistema forestal, incluyendo
    su identificación, apto médico, tareas asignadas y herramientas disponibles.
    Solo puede ejecutar tareas si tiene un apto médico vigente.
    
    Attributes:
        dni: Documento Nacional de Identidad del trabajador (identificador único).
        nombre: Nombre completo del trabajador.
        apto_medico: Certificación médica laboral del trabajador.
        tareas: Lista de tareas asignadas al trabajador (vacía por defecto).
        herramientas: Lista de herramientas asignadas al trabajador (vacía por defecto).
    """
    
    dni: int
    nombre: str
    apto_medico: AptoMedico
    tareas: List[Tarea] = field(default_factory=list)
    herramientas: List[Herramienta] = field(default_factory=list)
    
    def puede_trabajar(self) -> bool:
        """
        Verifica si el trabajador está habilitado para realizar tareas.
        
        Consulta el estado del apto médico para determinar si el trabajador
        puede ejecutar tareas de manera segura.
        
        Returns:
            True si el trabajador tiene apto médico vigente, False en caso contrario.
        """
        return self.apto_medico.es_apto
    
    def asignar_tarea(self, tarea: Tarea):
        """
        Añade una nueva tarea a la lista del trabajador.
        
        Asigna una tarea al trabajador solo si tiene apto médico vigente.
        Si no está apto, muestra un mensaje de error y no asigna la tarea.
        
        Args:
            tarea: Objeto Tarea a asignar al trabajador.
        """
        if self.puede_trabajar():
            self.tareas.append(tarea)
            print(f"Tarea '{tarea.descripcion}' asignada a {self.nombre}.")
        else:
            print(f"ERROR: {self.nombre} no puede recibir tareas por no tener apto médico vigente.")
    
    def ejecutar_tareas(self):
        """
        Ejecuta las tareas pendientes en orden descendente de ID.
        
        Procesa todas las tareas pendientes del trabajador, ordenándolas
        primero por ID de mayor a menor. Solo ejecuta si el trabajador
        tiene apto médico vigente. Marca cada tarea como COMPLETADA tras
        su ejecución.
        
        Raises:
            No lanza excepciones, pero muestra mensaje si el trabajador no puede trabajar.
        """
        if not self.puede_trabajar():
            print(f"{self.nombre} no puede trabajar.")
            return
        
        tareas_ordenadas = sorted(self.tareas, key=lambda t: t.id_tarea, reverse=True)
        
        print(f"\n--- {self.nombre} comienza a ejecutar tareas ---")
        for tarea in tareas_ordenadas:
            if tarea.estado == EstadoTarea.PENDIENTE:
                print(f"Ejecutando: '{tarea.descripcion}'...")
                tarea.estado = EstadoTarea.COMPLETADA
                print("Estado: COMPLETADA")
        print("-----------------------------------------")


################################################################################
# DIRECTORIO: entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/68: __init__.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/68: plantacion.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

import copy
from typing import List, TYPE_CHECKING

from ..cultivos.cultivo import Cultivo
from ...excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from ...excepciones.agua_agotada_exception import AguaAgotadaException

if TYPE_CHECKING:
    from ..personal.trabajador import Trabajador

class Plantacion:
    """
    Representa una plantación agrícola con gestión de cultivos y recursos.
    
    Administra los cultivos plantados, trabajadores asignados y recursos
    disponibles (agua y superficie). Implementa validaciones para garantizar
    que los recursos sean suficientes antes de realizar operaciones.
    
    Attributes:
        nombre: Nombre identificatorio de la plantación.
        superficie_disponible_m2: Superficie disponible en metros cuadrados.
        agua_disponible_litros: Cantidad de agua disponible en litros.
        cultivos: Lista de cultivos plantados en la plantación.
        trabajadores: Lista de trabajadores asignados a la plantación.
    """
    
    def __init__(self, nombre: str, superficie_disponible_m2: float, agua_disponible_litros: float = 500.0):
        """
        Inicializa una nueva plantación con sus recursos.
        
        Args:
            nombre: Nombre identificatorio de la plantación.
            superficie_disponible_m2: Superficie inicial disponible en metros cuadrados.
            agua_disponible_litros: Cantidad inicial de agua en litros. Por defecto 500.0.
        """
        self.nombre = nombre
        self.superficie_disponible_m2 = superficie_disponible_m2
        self.agua_disponible_litros = agua_disponible_litros
        self.cultivos: List[Cultivo] = []
        self.trabajadores: List['Trabajador'] = []

    def set_agua_disponible(self, nueva_cantidad: float):
        """
        Modifica la cantidad de agua disponible con validación.
        
        Actualiza el agua disponible en la plantación validando que
        no sea negativa. Cumple con el criterio de aceptación de US-002.
        
        Args:
            nueva_cantidad: Nueva cantidad de agua en litros (debe ser >= 0).
        
        Raises:
            ValueError: Si nueva_cantidad es negativa.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad de agua no puede ser negativa.")
        self.agua_disponible_litros = nueva_cantidad

    def get_cantidad_cultivos(self) -> int:
        """
        Devuelve el número total de cultivos en la plantación.
        
        Returns:
            Cantidad de cultivos plantados.
        """
        return len(self.cultivos)

    def plantar_cultivo(self, cultivo: Cultivo):
        """
        Añade un cultivo a la plantación si hay suficiente superficie.
        
        Valida que haya superficie disponible antes de plantar el cultivo.
        Si la plantación es exitosa, reduce la superficie disponible y
        añade el cultivo a la lista.
        
        Args:
            cultivo: Objeto Cultivo a plantar en la plantación.
        
        Raises:
            SuperficieInsuficienteException: Si no hay superficie suficiente
                                            para el cultivo.
        """
        if self.superficie_disponible_m2 < cultivo.metros_cuadrados_requeridos:
            raise SuperficieInsuficienteException(
                superficie_requerida=cultivo.metros_cuadrados_requeridos,
                superficie_disponible=self.superficie_disponible_m2
            )
        
        self.cultivos.append(cultivo)
        self.superficie_disponible_m2 -= cultivo.metros_cuadrados_requeridos
        print(f"PLANTACION: Se plantó '{cultivo.get_tipo()}'. Quedan {self.superficie_disponible_m2:.2f} m² disponibles.")

    def asignar_trabajador(self, trabajador: 'Trabajador'):
        """
        Asigna un trabajador a la plantación.
        
        Añade un trabajador a la lista de trabajadores de la plantación
        para que pueda ejecutar tareas en ella.
        
        Args:
            trabajador: Objeto Trabajador a asignar a la plantación.
        """
        self.trabajadores.append(trabajador)
        print(f"PLANTACION: Trabajador '{trabajador.nombre}' asignado a la plantación '{self.nombre}'.")
    
    def consumir_agua(self, litros_necesarios: float):
        """
        Consume agua de la reserva de la plantación con validación.
        
        Reduce la cantidad de agua disponible en la plantación. Si no hay
        suficiente agua, lanza una excepción antes de consumir.
        
        Args:
            litros_necesarios: Cantidad de agua a consumir en litros.
        
        Raises:
            AguaAgotadaException: Si no hay suficiente agua disponible.
        """
        if self.agua_disponible_litros < litros_necesarios:
            raise AguaAgotadaException(
                agua_requerida=litros_necesarios,
                agua_disponible=self.agua_disponible_litros
            )
        self.agua_disponible_litros -= litros_necesarios
        print(f"PLANTACION: Se consumieron {litros_necesarios:.2f}L. Quedan {self.agua_disponible_litros:.2f}L.")
    
    def set_trabajadores(self, lista_trabajadores: List['Trabajador']):
        """
        Reemplaza la lista de trabajadores con copia defensiva.
        
        Asigna una nueva lista de trabajadores a la plantación, creando
        una copia para mantener inmutabilidad. Cumple con US-017.
        
        Args:
            lista_trabajadores: Lista de trabajadores a asignar a la plantación.
        """
        self.trabajadores = copy.copy(lista_trabajadores)
        print(f"INFO: Se asignaron {len(self.trabajadores)} trabajadores a '{self.nombre}'.")

    def get_trabajadores(self) -> List['Trabajador']:
        """
        Devuelve una copia inmutable de la lista de trabajadores.
        
        Retorna una copia de la lista de trabajadores para prevenir
        modificaciones externas. Cumple con US-014.
        
        Returns:
            Copia de la lista de trabajadores asignados a la plantación.
        """
        return copy.copy(self.trabajadores)

# ==============================================================================
# ARCHIVO 21/68: registro_forestal.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\registro_forestal.py
# ==============================================================================

from dataclasses import dataclass
from .tierra import Tierra
from .plantacion import Plantacion

@dataclass
class RegistroForestal:
    """
    Entidad principal que vincula un terreno con su plantación.
    
    Representa el registro oficial completo de una propiedad forestal,
    incluyendo datos del propietario, avalúo fiscal, información del
    terreno y detalles de la plantación asociada.
    
    Attributes:
        propietario: Nombre completo del propietario del terreno.
        avaluo_fiscal: Valor fiscal del terreno para fines impositivos.
        tierra: Objeto Tierra con la información catastral del terreno.
        plantacion: Objeto Plantacion con los cultivos y trabajadores.
    """
    
    propietario: str
    avaluo_fiscal: float
    tierra: Tierra
    plantacion: Plantacion

    def mostrar_datos(self):
        """
        Imprime en consola los datos del registro con formato específico.
        
        Muestra de manera estructurada toda la información del registro
        forestal, incluyendo datos catastrales, propietario, avalúo y
        cantidad de cultivos. Cumple con el criterio de aceptación de US-003.
        """
        print("\nREGISTRO FORESTAL")
        print("=" * 17)
        print(f"Padron:      {self.tierra.padron_catastral}")
        print(f"Propietario: {self.propietario}")
        print(f"Avaluo:      {self.avaluo_fiscal}")
        print(f"Domicilio:   {self.tierra.domicilio}")
        print(f"Superficie:  {self.tierra.superficie_m2}")
        print(f"Cantidad de cultivos plantados: {self.plantacion.get_cantidad_cultivos()}")  # pylint: disable=no-member
        print("=" * 17)

# ==============================================================================
# ARCHIVO 22/68: tierra.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\tierra.py
# ==============================================================================

class Tierra:
    """
    Representa un terreno catastral con su información legal y física.
    
    Gestiona los datos catastrales de un terreno forestal, incluyendo su
    identificación única (padrón), superficie y ubicación. Incluye validación
    interna para garantizar datos consistentes.
    
    Attributes:
        _padron_catastral: Identificador único del terreno en el registro catastral.
        _superficie_m2: Superficie del terreno en metros cuadrados (debe ser positiva).
        _domicilio: Dirección o ubicación geográfica del terreno.
    
    Raises:
        ValueError: Si la superficie es menor o igual a cero durante la inicialización.
    """
    
    def __init__(self, padron_catastral: str, superficie_m2: float, domicilio: str):
        """
        Inicializa un nuevo terreno con validación de superficie.
        
        Args:
            padron_catastral: Identificador catastral único del terreno.
            superficie_m2: Superficie del terreno en metros cuadrados (debe ser > 0).
            domicilio: Dirección o ubicación geográfica del terreno.
        
        Raises:
            ValueError: Si superficie_m2 es menor o igual a cero.
        """
        if superficie_m2 <= 0:
            raise ValueError("La superficie debe ser un número positivo.")
        
        self._padron_catastral = padron_catastral
        self._superficie_m2 = superficie_m2
        self._domicilio = domicilio

    @property
    def padron_catastral(self) -> str:
        """
        Obtiene el padrón catastral del terreno.
        
        Returns:
            Identificador catastral único del terreno.
        """
        return self._padron_catastral

    @property
    def superficie_m2(self) -> float:
        """
        Obtiene la superficie del terreno en metros cuadrados.
        
        Returns:
            Superficie en metros cuadrados.
        """
        return self._superficie_m2

    @property
    def domicilio(self) -> str:
        """
        Obtiene el domicilio o ubicación del terreno.
        
        Returns:
            Dirección geográfica del terreno.
        """
        return self._domicilio

    def set_superficie(self, nueva_superficie_m2: float):
        """
        Modifica la superficie del terreno con validación.
        
        Actualiza la superficie del terreno validando que el nuevo valor
        sea positivo. Cumple con el criterio de aceptación de US-001.
        
        Args:
            nueva_superficie_m2: Nueva superficie en metros cuadrados (debe ser > 0).
        
        Raises:
            ValueError: Si nueva_superficie_m2 es menor o igual a cero.
        """
        if nueva_superficie_m2 <= 0:
            raise ValueError("La superficie debe ser un número positivo.")
        self._superficie_m2 = nueva_superficie_m2
        print(f"INFO: La superficie del padrón {self._padron_catastral} se actualizó a {self._superficie_m2} m².")



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/68: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/68: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\agua_agotada_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua para completar una operación.
    
    Se utiliza cuando se intenta realizar un riego u otra operación que requiere
    agua, pero la plantación no tiene suficientes recursos hídricos disponibles.
    Proporciona información detallada sobre la cantidad requerida versus la disponible.
    
    Attributes:
        _requerida: Cantidad de agua necesaria para la operación en litros.
        _disponible: Cantidad de agua actualmente disponible en litros.
    """
    
    def __init__(self, agua_requerida: float, agua_disponible: float):
        """
        Inicializa una excepción de agua agotada con cantidades específicas.
        
        Args:
            agua_requerida: Cantidad de agua necesaria en litros.
            agua_disponible: Cantidad de agua disponible en litros.
        """
        self._requerida = agua_requerida
        self._disponible = agua_disponible
       
        mensaje = (f"Recursos hídricos insuficientes. Requerido: {self._requerida:.2f}L, "
                   f"Disponible: {self._disponible:.2f}L.")
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Returns:
            Mensaje amigable indicando falta de agua.
        """
        return "Agua insuficiente para completar el riego."

    def get_agua_requerida(self) -> float:
        """
        Obtiene la cantidad de agua que se requería para la operación.
        
        Returns:
            Cantidad de agua requerida en litros.
        """
        return self._requerida

    def get_agua_disponible(self) -> float:
        """
        Obtiene la cantidad de agua actualmente disponible.
        
        Returns:
            Cantidad de agua disponible en litros.
        """
        return self._disponible


# ==============================================================================
# ARCHIVO 25/68: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """
    Excepción base para todos los errores del sistema de forestación.
    
    Clase raíz de la jerarquía de excepciones personalizadas del dominio forestal.
    Todas las excepciones específicas (SuperficieInsuficienteException,
    AguaAgotadaException, PersistenciaException) heredan de esta clase,
    permitiendo un manejo unificado de errores mediante catch polimórfico.
    
    Esta excepción implementa separación de mensajes:
    - Usuario: Mensaje simplificado y amigable
    - Técnico: Mensaje detallado con contexto técnico
    
    Attributes:
        mensaje: Descripción completa del error (mensaje técnico).
    
    
    """
    
    def __init__(self, mensaje: str = "Ha ocurrido un error en el sistema de forestación."):
        """
        Inicializa una excepción de forestación con mensaje descriptivo.
        
        Args:
            mensaje: Descripción técnica del error. Por defecto es un mensaje genérico.
        """
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def get_full_message(self) -> str:
        """
        Obtiene el mensaje técnico completo del error.
        
        Proporciona información detallada para logs, debugging y diagnóstico técnico.
        
        Returns:
            Mensaje de error completo como cadena de texto.

        """
        return self.mensaje

# ==============================================================================
# ARCHIVO 26/68: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\mensajes_exception.py
# ==============================================================================

class MensajesException:
    """
    Clase de utilidad que centraliza mensajes de error del sistema.
    
    Define constantes con mensajes de error estandarizados para garantizar
    consistencia en los mensajes mostrados al usuario. Los mensajes utilizan
    formato de cadena para permitir interpolación de valores dinámicos.
    
    Attributes:
        ESPECIE_DESCONOCIDA: Mensaje cuando se intenta crear un cultivo de especie no reconocida.
        SERVICIO_NO_REGISTRADO: Mensaje cuando no existe servicio para un tipo de cultivo.
        PADRON_DUPLICADO: Mensaje cuando se intenta registrar un padrón catastral duplicado.
    """
   
    ESPECIE_DESCONOCIDA = "Especie de cultivo desconocida: '{}'"
    """Mensaje de error para especie de cultivo no reconocida. Requiere 1 parámetro: nombre de especie."""
    
    SERVICIO_NO_REGISTRADO = "No hay un servicio registrado para el cultivo: '{}'"
    """Mensaje de error para cultivo sin servicio registrado. Requiere 1 parámetro: tipo de cultivo."""
    
    PADRON_DUPLICADO = "El padrón catastral '{}' ya existe en el sistema."
    """Mensaje de error para padrón catastral duplicado. Requiere 1 parámetro: número de padrón."""

# ==============================================================================
# ARCHIVO 27/68: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\persistencia_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepción lanzada cuando ocurre un error durante operaciones de persistencia.
    
    Se utiliza para encapsular errores que ocurren durante la serialización,
    deserialización o cualquier operación de E/S relacionada con el almacenamiento
    de datos en disco. Mantiene referencia a la causa original del error para
    facilitar el diagnóstico.
    
    Attributes:
        _operacion: Tipo de operación que falló (ej. "ESCRITURA", "LECTURA").
        _causa: Excepción original que causó el error de persistencia.
    """
    
    def __init__(self, operacion: str, causa: Exception):
        """
        Inicializa una excepción de persistencia con contexto del error.
        
        Args:
            operacion: Nombre de la operación que falló (ej. "ESCRITURA", "LECTURA").
            causa: Excepción original que causó el fallo.
        """
        self._operacion = operacion
        self._causa = causa
       
        mensaje = f"Error durante la operación de persistencia '{self._operacion}'. Causa: {self._causa}"
        super().__init__(mensaje)
       
    def get_operacion(self) -> str:
        """
        Obtiene el tipo de operación de persistencia que falló.
        
        Returns:
            Nombre de la operación (ej. "ESCRITURA", "LECTURA").
        """
        return self._operacion
       
    def get_causa_original(self) -> Exception:
        """
        Obtiene la excepción original que causó el error.
        
        Permite acceder a la excepción subyacente (ej. IOError, PickleError)
        para obtener más detalles sobre el fallo.
        
        Returns:
            Excepción original que causó el error de persistencia.
        """
        return self._causa


# ==============================================================================
# ARCHIVO 28/68: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie para plantar un cultivo.
    
    Se utiliza cuando se intenta plantar un cultivo pero la plantación no tiene
    suficiente superficie disponible. Proporciona información detallada sobre:
    - Superficie requerida por el cultivo
    - Superficie disponible en la plantación
    - Diferencia (déficit de superficie)
    
    Esta excepción cumple con el criterio de aceptación de US-004 que especifica:
    "Si no hay superficie, lanzar SuperficieInsuficienteException".
    
    Attributes:
        _requerida: Superficie necesaria para el cultivo en metros cuadrados.
        _disponible: Superficie actualmente disponible en metros cuadrados.
 

    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa una excepción de superficie insuficiente con valores específicos.
        
        Construye mensajes técnicos detallados incluyendo las cantidades exactas
        de superficie requerida versus disponible para facilitar el diagnóstico.
        
        Args:
            superficie_requerida: Superficie necesaria en metros cuadrados (debe ser > 0).
            superficie_disponible: Superficie disponible en metros cuadrados (debe ser >= 0).

        """
        self._requerida = superficie_requerida
        self._disponible = superficie_disponible
       
        mensaje = (
            f"Superficie insuficiente. "
            f"Requerido: {self._requerida:.2f} m², "
            f"Disponible: {self._disponible:.2f} m². "
            f"Déficit: {(self._requerida - self._disponible):.2f} m²"
        )
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Proporciona un mensaje amigable sin detalles técnicos para
        interfaces de usuario o reportes orientados a usuarios no técnicos.
        
        Returns:
            Mensaje simplificado indicando falta de superficie.
  
        """
        return "Superficie insuficiente para plantar."

    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie que se requería para plantar el cultivo.
        
        Útil para cálculos de expansión o re-planificación de plantaciones.
        
        Returns:
            Superficie requerida en metros cuadrados.
   
        """
        return self._requerida

    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie actualmente disponible en la plantación.
        
        Permite al código cliente tomar decisiones sobre cuántos cultivos
        alternativos podrían plantarse con la superficie disponible.
        
        Returns:
            Superficie disponible en metros cuadrados.

        """
        return self._disponible
    
    def get_deficit(self) -> float:
        """
        Calcula el déficit de superficie (cuánto falta).
        
        Returns:
            Diferencia entre requerido y disponible en metros cuadrados.
  
        """
        return self._requerida - self._disponible


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/68: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 30/68: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/68: cultivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\factory\cultivo_factory.py
# ==============================================================================

from typing import Dict, Callable
from ...entidades.cultivos.cultivo import Cultivo
from ...entidades.cultivos.pino import Pino
from ...entidades.cultivos.olivo import Olivo
from ...entidades.cultivos.lechuga import Lechuga
from ...entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    """
    Implementa el patrón Factory Method para crear instancias de cultivos.
    
    Centraliza la lógica de creación de diferentes tipos de cultivos,
    desacoplando el código cliente de las clases concretas mediante
    el uso de métodos estáticos dedicados en lugar de lambdas.
    
    El patrón Factory Method cumple con:
    - Open/Closed Principle: Extensible sin modificar código existente
    - Dependency Inversion: Cliente depende de abstracción (Cultivo)
    - Single Responsibility: Solo responsable de crear cultivos
    
    Attributes:
        _factories: Diccionario que mapea nombres de especies a métodos de creación.
    
    Example:
        >>> cultivo = CultivoFactory.crear_cultivo("Pino")
        >>> isinstance(cultivo, Pino)
        True
    """
    
    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Crea una instancia de Pino con configuración por defecto.
        
        Returns:
            Nueva instancia de Pino con variedad "Parana".
        """
        return Pino()
    
    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Crea una instancia de Olivo con configuración por defecto.
        
        Returns:
            Nueva instancia de Olivo con tipo de aceituna ARBEQUINA.
        """
        return Olivo()
    
    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Crea una instancia de Lechuga con configuración por defecto.
        
        Returns:
            Nueva instancia de Lechuga con variedad "Invernadero".
        """
        return Lechuga()
    
    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Crea una instancia de Zanahoria con configuración por defecto.
        
        Returns:
            Nueva instancia de Zanahoria tipo regular (no baby).
        """
        return Zanahoria()
    
    _factories: Dict[str, Callable[[], Cultivo]] = {
        "pino": _crear_pino.__func__,           
        "olivo": _crear_olivo.__func__,         
        "lechuga": _crear_lechuga.__func__,     
        "zanahoria": _crear_zanahoria.__func__  
    }

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea una instancia de cultivo según la especie especificada.
        
        Método principal del Factory que actúa como punto de entrada único
        para la creación de cultivos. Utiliza dispatch mediante diccionario
        para delegar la creación al método específico correspondiente.
        
        Este diseño permite agregar nuevos tipos de cultivos sin modificar
        el código cliente, cumpliendo con el Open/Closed Principle.
        
        Args:
            especie: Nombre del tipo de cultivo a crear. No es sensible a
                    mayúsculas/minúsculas. Valores válidos: "Pino", "Olivo",
                    "Lechuga", "Zanahoria".
        
        Returns:
            Instancia de Cultivo del tipo solicitado (Pino, Olivo, Lechuga o Zanahoria).
        
        Raises:
            ValueError: Si la especie solicitada no está registrada en el factory.
        
        Example:
            >>> pino = CultivoFactory.crear_cultivo("Pino")
            >>> olivo = CultivoFactory.crear_cultivo("olivo")  # Case insensitive
            >>> lechuga = CultivoFactory.crear_cultivo("LECHUGA")
        
        Note:
            El factory retorna el tipo base Cultivo para mantener el desacoplamiento,
            aunque internamente crea instancias de tipos concretos.
        """
        especie_lower = especie.lower()
        
        if especie_lower not in CultivoFactory._factories:
            raise ValueError(
                f"Especie de cultivo desconocida: '{especie}'. "
                f"Especies válidas: {', '.join(CultivoFactory._factories.keys())}"
            )
        
        return CultivoFactory._factories[especie_lower]()


################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 32/68: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/68: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\observable.py
# ==============================================================================

from typing import List, TypeVar, Generic
from .observer import Observer

T = TypeVar('T')

class Observable(Generic[T]):
    """
    Implementación del patrón Observer que permite notificar cambios a múltiples observadores.
    
    Esta clase genérica permite a los objetos Observable notificar a sus observadores registrados
    cuando ocurre un evento. Utiliza generics para garantizar type-safety, asegurando que el tipo
    de evento notificado coincida con el tipo esperado por los observadores.
    
    El patrón Observer es utilizado en el sistema de riego automatizado, donde los sensores
    de temperatura y humedad actúan como Observable[float], notificando lecturas al controlador
    de riego que actúa como Observer[float].
    
    Type Parameters:
        T: Tipo de dato del evento que será notificado a los observadores.
    
    Attributes:
        _observadores: Lista de observadores suscritos a este observable.
    
    """

    def __init__(self):
        """
        Inicializa un nuevo Observable con lista vacía de observadores.
        """
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Registra un observador para recibir notificaciones de eventos.
        
        El observador solo se agrega si no está ya registrado, evitando duplicados.
        Una vez registrado, recibirá notificaciones cada vez que se llame a
        notificar_observadores().
        
        Args:
            observador: Instancia de Observer[T] que será notificada de eventos.

        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def quitar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista de suscritos.
        
        Después de quitarlo, el observador ya no recibirá notificaciones de eventos.
        Si el observador no está registrado, lanza ValueError.
        
        Args:
            observador: Instancia de Observer[T] a eliminar.
        
        Raises:
            ValueError: Si el observador no está en la lista de observadores.
        """
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores registrados sobre un evento ocurrido.
        
        Itera sobre la lista de observadores y llama al método actualizar() de cada uno,
        pasando el evento como parámetro. El evento debe ser del tipo T especificado
        en la declaración del Observable.
        
        En el sistema de riego, este método es llamado cada vez que un sensor lee
        un nuevo valor (temperatura o humedad), notificando al controlador de riego.
        
        Args:
            evento: Dato del evento a notificar (debe ser de tipo T).
        

        """
        print(f"OBSERVABLE: Notificando a {len(self._observadores)} observador(es)...")
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 34/68: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    Interfaz del patrón Observer para objetos que reciben notificaciones de eventos.
    
    Define el contrato que deben cumplir todos los observadores en el sistema.
    Los observadores se suscriben a objetos Observable y reciben notificaciones
    automáticas cuando ocurren eventos mediante el método actualizar().
    
    Esta clase abstracta genérica garantiza type-safety, asegurando que el tipo
    de evento recibido coincida con el tipo esperado por el observador.
    
    En el sistema de riego automatizado, ControlRiegoTask implementa Observer[float]
    para recibir lecturas de los sensores de temperatura y humedad.
    
    Type Parameters:
        T: Tipo de dato del evento que será recibido por el observador.

    """
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método abstracto que recibe notificaciones cuando ocurre un evento.
        
        Este método es llamado automáticamente por el Observable cuando se invoca
        notificar_observadores(). Las implementaciones concretas deben definir
        la lógica de respuesta al evento recibido.
        
        En el sistema de riego, ControlRiegoTask implementa este método para:
        - Actualizar valores de temperatura/humedad
        - Evaluar condiciones de riego
        - Activar riego automático si las condiciones se cumplen
        
        Args:
            evento: Dato del evento notificado (debe ser de tipo T).
        
        """
        pass


################################################################################
# DIRECTORIO: patrones\observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/68: __init__.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\eventos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/68: evento_plantacion.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ==============================================================================

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....entidades.cultivos.cultivo import Cultivo
    from ....entidades.terrenos.plantacion import Plantacion


class TipoEventoPlantacion(Enum):
    """
    Enumeración de tipos de eventos que pueden ocurrir en una plantación.
    
    Define los diferentes eventos del ciclo de vida de una plantación que
    podrían ser monitoreados por observadores en el sistema.
    
    Attributes:
        CULTIVO_PLANTADO: Se plantó un nuevo cultivo en la plantación.
        RIEGO_REALIZADO: Se completó una operación de riego.
        CULTIVO_COSECHADO: Se cosechó un cultivo de la plantación.
        FUMIGACION_APLICADA: Se aplicó un plaguicida a la plantación.
        AGUA_AGOTADA: El agua disponible cayó por debajo del umbral crítico.
        SUPERFICIE_INSUFICIENTE: No hay suficiente superficie para plantar.
    """
    CULTIVO_PLANTADO = auto()
    RIEGO_REALIZADO = auto()
    CULTIVO_COSECHADO = auto()
    FUMIGACION_APLICADA = auto()
    AGUA_AGOTADA = auto()
    SUPERFICIE_INSUFICIENTE = auto()


@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación agrícola.
    
    Encapsula información completa sobre eventos del ciclo de vida de una
    plantación, permitiendo un sistema de logging, auditoría y notificaciones
    más robusto que el actual.
    
    Esta clase es opcional y actualmente no se utiliza en el sistema principal.
    Se proporciona como extensión para futuras implementaciones que requieran:
    - Logging detallado de operaciones
    - Auditoría completa de cambios en plantaciones
    - Sistema de notificaciones a múltiples observadores
    - Dashboard de monitoreo en tiempo real
    - Análisis histórico de operaciones
    

    Attributes:
        tipo: Tipo de evento que ocurrió en la plantación.
        plantacion: Plantación donde ocurrió el evento.
        timestamp: Momento exacto del evento.
        descripcion: Descripción textual del evento para logging.
        cultivo_relacionado: Cultivo involucrado en el evento (opcional).
        datos_adicionales: Diccionario con información adicional (opcional).
    """
    tipo: TipoEventoPlantacion
    plantacion: 'Plantacion'
    timestamp: datetime
    descripcion: str
    cultivo_relacionado: 'Cultivo' = None
    datos_adicionales: dict = None

    def __str__(self) -> str:
        """
        Representación en cadena legible del evento.
        
        Returns:
            Cadena formateada con tipo, plantación, timestamp y descripción.

        """
        plantacion_nombre = self.plantacion.nombre if self.plantacion else "Desconocida"
        timestamp_str = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        resultado = (f"[{self.tipo.name}] Plantación '{plantacion_nombre}' - {timestamp_str}\n"
                    f"Descripción: {self.descripcion}")
        
        if self.cultivo_relacionado:
            resultado += f"\nCultivo: {self.cultivo_relacionado.get_tipo()}"
        
        if self.datos_adicionales:
            resultado += f"\nDatos adicionales: {self.datos_adicionales}"
        
        return resultado

    def es_evento_critico(self) -> bool:
        """
        Determina si el evento requiere atención inmediata.
        
        Los eventos críticos son aquellos que indican problemas o situaciones
        que requieren intervención del operador del sistema.
        
        Returns:
            True si es evento crítico (agua agotada o superficie insuficiente).

        """
        return self.tipo in {
            TipoEventoPlantacion.AGUA_AGOTADA,
            TipoEventoPlantacion.SUPERFICIE_INSUFICIENTE
        }

    def es_evento_operacional(self) -> bool:
        """
        Determina si el evento es parte de operaciones normales.
        
        Los eventos operacionales son operaciones rutinarias del sistema
        que no requieren atención especial.
        
        Returns:
            True si es evento operacional (plantado, riego, cosecha, fumigación).

        """
        return self.tipo in {
            TipoEventoPlantacion.CULTIVO_PLANTADO,
            TipoEventoPlantacion.RIEGO_REALIZADO,
            TipoEventoPlantacion.CULTIVO_COSECHADO,
            TipoEventoPlantacion.FUMIGACION_APLICADA
        }

    @staticmethod
    def crear_evento_plantado(plantacion: 'Plantacion', cultivo: 'Cultivo') -> 'EventoPlantacion':
        """
        Factory method para crear un evento de plantación de cultivo.
        
        Args:
            plantacion: Plantación donde se plantó el cultivo.
            cultivo: Cultivo que fue plantado.
        
        Returns:
            EventoPlantacion configurado para plantación de cultivo.

        """
        return EventoPlantacion(
            tipo=TipoEventoPlantacion.CULTIVO_PLANTADO,
            plantacion=plantacion,
            timestamp=datetime.now(),
            descripcion=f"Se plantó {cultivo.get_tipo()} en la plantación",
            cultivo_relacionado=cultivo
        )

    @staticmethod
    def crear_evento_riego(plantacion: 'Plantacion', litros_consumidos: float) -> 'EventoPlantacion':
        """
        Factory method para crear un evento de riego.
        
        Args:
            plantacion: Plantación que fue regada.
            litros_consumidos: Cantidad de agua utilizada en el riego.
        
        Returns:
            EventoPlantacion configurado para riego.
 
        """
        return EventoPlantacion(
            tipo=TipoEventoPlantacion.RIEGO_REALIZADO,
            plantacion=plantacion,
            timestamp=datetime.now(),
            descripcion=f"Se realizó riego con {litros_consumidos} litros",
            datos_adicionales={"litros_consumidos": litros_consumidos}
        )

    @staticmethod
    def crear_evento_agua_agotada(plantacion: 'Plantacion', agua_disponible: float) -> 'EventoPlantacion':
        """
        Factory method para crear un evento de agua agotada (crítico).
        
        Args:
            plantacion: Plantación con agua agotada.
            agua_disponible: Cantidad de agua restante (debajo del umbral).
        
        Returns:
            EventoPlantacion configurado para agua agotada.

        """
        return EventoPlantacion(
            tipo=TipoEventoPlantacion.AGUA_AGOTADA,
            plantacion=plantacion,
            timestamp=datetime.now(),
            descripcion=f"ALERTA: Agua agotada. Disponible: {agua_disponible}L",
            datos_adicionales={"agua_disponible": agua_disponible}
        )

# ==============================================================================
# ARCHIVO 37/68: evento_sensor.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ==============================================================================

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class TipoSensor(Enum):
    """
    Enumeración de tipos de sensores ambientales del sistema de riego.
    
    Define los tipos de sensores que pueden generar eventos en el
    sistema de monitoreo automatizado.
    
    Attributes:
        TEMPERATURA: Sensor que mide temperatura ambiental en °C.
        HUMEDAD: Sensor que mide humedad relativa del aire en %.
    """
    TEMPERATURA = auto()
    HUMEDAD = auto()


@dataclass
class EventoSensor:
    """
    Representa un evento generado por un sensor ambiental.
    
    Encapsula la información completa de una lectura de sensor, incluyendo
    el tipo de sensor, el valor medido y el timestamp de la lectura.
    
    Esta clase es opcional y actualmente no se utiliza en el sistema,
    ya que los sensores notifican directamente valores float mediante
    Observable[float]. Sin embargo, se proporciona como ejemplo de cómo
    se podrían estructurar eventos más complejos en futuras versiones.
    
    Uso potencial:
    - Logging detallado de lecturas con timestamps
    - Auditoría de eventos del sistema de riego
    - Análisis histórico de condiciones ambientales
    - Debugging y troubleshooting
    
    Attributes:
        tipo_sensor: Tipo de sensor que generó el evento (TEMPERATURA o HUMEDAD).
        valor: Valor medido por el sensor (°C para temperatura, % para humedad).
        timestamp: Momento exacto en que se realizó la lectura.
        unidad: Unidad de medida del valor ("°C" o "%").

    """
    tipo_sensor: TipoSensor
    valor: float
    timestamp: datetime
    unidad: str

    def __str__(self) -> str:
        """
        Representación en cadena legible del evento.
        
        Returns:
            Cadena formateada con tipo, valor, unidad y timestamp.

        """
        return (f"[{self.tipo_sensor.name}] {self.valor}{self.unidad} - "
                f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    def es_temperatura(self) -> bool:
        """
        Verifica si el evento proviene de un sensor de temperatura.
        
        Returns:
            True si es evento de temperatura, False en caso contrario.

        """
        return self.tipo_sensor == TipoSensor.TEMPERATURA

    def es_humedad(self) -> bool:
        """
        Verifica si el evento proviene de un sensor de humedad.
        
        Returns:
            True si es evento de humedad, False en caso contrario.

        """
        return self.tipo_sensor == TipoSensor.HUMEDAD


################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/68: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\singleton\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 39/68: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/68: absorcion_agua_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 41/68: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/68: absorcion_constante_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 43/68: absorcion_seasonal_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 44/68: __init__.py
# Directorio: riego
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego\control
################################################################################

# ==============================================================================
# ARCHIVO 45/68: __init__.py
# Directorio: riego\control
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/68: control_riego_task.py
# Directorio: riego\control
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\riego\control\control_riego_task.py
# ==============================================================================

import threading
import time
from typing import Optional

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.constantes import (
    TEMP_MIN_RIEGO,  
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO,
    INTERVALO_CONTROL_RIEGO,
    SENSOR_TEMP_MAX
)

class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador automatizado de riego que implementa el patrón Observer.
    
    Opera como un hilo daemon que observa continuamente los sensores de temperatura
    y humedad, evaluando las condiciones ambientales y activando el riego automático
    cuando se cumplen los criterios establecidos.
    
    Este controlador representa el núcleo del sistema de riego inteligente, tomando
    decisiones basadas en datos en tiempo real. Implementa el patrón Observer para
    recibir notificaciones de ambos sensores y el patrón Thread para operar de forma
    asíncrona sin bloquear el resto del sistema.
    
    Condiciones de riego automático:
    - Temperatura entre 8°C y 15°C (TEMP_MIN_RIEGO y TEMP_MAX_RIEGO)
    - Humedad menor a 50% (HUMEDAD_MAX_RIEGO)
    - Ambas condiciones deben cumplirse simultáneamente
    
    El controlador evalúa las condiciones cada 2.5 segundos (INTERVALO_CONTROL_RIEGO)
    y delega la operación de riego al PlantacionService, garantizando separación
    de responsabilidades y mantenibilidad del código.
    
    Attributes:
        _ultima_temperatura: Última lectura de temperatura recibida del sensor (°C).
        _ultima_humedad: Última lectura de humedad recibida del sensor (%).
        _plantacion: Plantación sobre la cual se ejecutará el riego.
        _plantacion_service: Servicio que ejecuta la lógica de riego.
        _detenido: Event para detención controlada del hilo.
    """
    
    def __init__(
        self,
        sensor_temp: TemperaturaReaderTask,
        sensor_hum: HumedadReaderTask,
        plantacion: Plantacion,
        plantacion_service: PlantacionService
    ):
        """
        Inicializa el controlador de riego e inyecta dependencias.
        
        El controlador se registra automáticamente como observador de ambos sensores
        mediante el patrón Observer, garantizando que recibirá notificaciones de
        todas las lecturas realizadas.
        
        Este diseño cumple con Dependency Injection, permitiendo testear el
        controlador con sensores mock y servicios simulados.
        
        Args:
            sensor_temp: Sensor de temperatura (Observable[float]) que notificará lecturas.
            sensor_hum: Sensor de humedad (Observable[float]) que notificará lecturas.
            plantacion: Plantación objetivo donde se ejecutará el riego.
            plantacion_service: Servicio que contiene la lógica de negocio del riego.
        """
        threading.Thread.__init__(self)
        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        
        sensor_temp.agregar_observador(self)
        sensor_hum.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Recibe notificaciones de los sensores e identifica el tipo de lectura.
        
        Implementa el método requerido por la interfaz Observer[float]. Recibe
        valores de temperatura o humedad y los almacena en el estado interno.
        
        La distinción entre temperatura y humedad se realiza mediante análisis
        del rango de valores:
        - Temperatura: valores <= SENSOR_TEMP_MAX (50°C)
        - Humedad: valores > SENSOR_TEMP_MAX (porcentajes hasta 100%)
        
        Este método es llamado automáticamente por los sensores cada vez que
        realizan una lectura, garantizando que el controlador siempre trabaja
        con datos actualizados.
        
        Args:
            evento: Valor numérico de la lectura del sensor (temperatura en °C
                   o humedad en porcentaje).
        
        """
        if evento <= SENSOR_TEMP_MAX: 
             print(f"CONTROLADOR: Notificación de temperatura recibida -> {evento}°C")
             self._ultima_temperatura = evento
        else:
             print(f"CONTROLADOR: Notificación de humedad recibida -> {evento}%")
             self._ultima_humedad = evento

    def _evaluar_condiciones_y_regar(self):
        """
        Evalúa las condiciones ambientales y activa riego si corresponde.
        
        Método privado que contiene la lógica de decisión del sistema de riego
        automatizado. Verifica:
        
        1. Que existan lecturas de ambos sensores (no None)
        2. Que la temperatura esté en el rango óptimo (8°C - 15°C)
        3. Que la humedad sea inferior al umbral (< 50%)
        
        Si todas las condiciones se cumplen, delega la operación de riego al
        PlantacionService. Si no hay agua disponible, captura la excepción
        AguaAgotadaException y registra el error sin detener el sistema.
        
        Este diseño permite que el controlador continúe operando incluso si
        ocurren errores puntuales, garantizando resiliencia del sistema.
        
        Raises:
            No lanza excepciones - las captura internamente para no detener el hilo.
        
        """
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            print("CONTROLADOR: Esperando lecturas iniciales de ambos sensores...")
            return

        print(f"CONTROLADOR: Evaluando T={self._ultima_temperatura}°C, H={self._ultima_humedad}%")
        
        if (TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO and
            self._ultima_humedad < HUMEDAD_MAX_RIEGO):
            print("CONTROLADOR: ¡Condiciones óptimas! Iniciando riego...")
            try:
                self._plantacion_service.regar_plantacion(self._plantacion)
                print("CONTROLADOR: ¡RIEGO COMPLETADO!")
            except Exception as e:
                print(f"CONTROLADOR ERROR: No se pudo regar. Causa: {e}")
        else:
            print("CONTROLADOR: Condiciones no aptas para el riego.")

    def run(self):
        """
        Ejecuta el bucle principal del controlador en segundo plano.
        
        Este método es invocado automáticamente cuando se llama a start() en el hilo.
        Implementa un bucle infinito que evalúa condiciones de riego periódicamente
        cada INTERVALO_CONTROL_RIEGO (2.5 segundos).
        
        El bucle continúa hasta que se invoca detener(), momento en el cual el
        Event _detenido es activado y el bucle termina de forma controlada.
        
        """
        print("CONTROLADOR: El sistema de control de riego ha comenzado a operar.")
        while not self._detenido.is_set():
            self._evaluar_condiciones_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)

    def detener(self):
        """
        Detiene el controlador de forma segura mediante señalización.
        
        Activa el Event _detenido, señalizando al bucle en run() que debe
        finalizar en su próxima iteración. Este diseño garantiza graceful shutdown,
        permitiendo que el hilo complete su operación actual antes de terminar.
        
        Después de invocar este método, se recomienda llamar a join() con timeout
        para esperar la finalización del hilo:
        
        """
        print("CONTROLADOR: Deteniendo el sistema de control de riego.")
        self._detenido.set()


################################################################################
# DIRECTORIO: riego\sensores
################################################################################

# ==============================================================================
# ARCHIVO 47/68: __init__.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 48/68: humedad_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\riego\sensores\humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)

class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de humedad que realiza lecturas periódicas implementando el patrón Observer.

    Características del sensor:
    - Rango de medición: 0% a 100% (SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)
    - Intervalo de lectura: 3 segundos (INTERVALO_SENSOR_HUMEDAD)
    - Precisión simulada: 2 decimales
    - Modo de operación: Asíncrono mediante threading
    
    Attributes:
        _detenido: Event para señalización de detención controlada del hilo.
        _observadores: Lista de observadores heredada de Observable[float].
    
    """
    
    def __init__(self):
        """
        Inicializa el sensor de humedad como hilo daemon y observable.
        
        Realiza la inicialización múltiple requerida por herencia múltiple de
        threading.Thread y Observable[float]. El Event _detenido permite
        implementar graceful shutdown del hilo.
        
        El sensor comienza sin observadores registrados; estos deben agregarse
        mediante agregar_observador() antes de iniciar el hilo para recibir
        notificaciones.
        
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        """
        Simula la lectura del sensor de humedad ambiental.
        
        Genera un valor aleatorio dentro del rango válido de humedad definido
        en las constantes del sistema (0% a 100%). En un sistema real, este
        método se conectaría a hardware físico mediante GPIO, I2C, o protocolos
        similares.
        
        La simulación utiliza distribución uniforme para generar valores
        realistas en todo el rango posible, permitiendo probar el sistema
        con diversos escenarios de humedad sin necesidad de hardware real.
        
        Returns:
            Porcentaje de humedad ambiental redondeado a 2 decimales (0.00 - 100.00).

        """
        return round(random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX), 2)

    def run(self):
        """
        Ejecuta el bucle de lectura continua del sensor en segundo plano.
        
        Este método es invocado automáticamente cuando se llama a start() en el hilo.
        Implementa un ciclo infinito que:
        
        1. Lee el valor actual de humedad mediante _leer_humedad()
        2. Registra la lectura en consola para trazabilidad
        3. Notifica el valor a todos los observadores registrados
        4. Espera INTERVALO_SENSOR_HUMEDAD (3 segundos) antes de la próxima lectura
        
        El ciclo continúa hasta que se invoca detener(), momento en el cual el
        Event _detenido es activado y el bucle termina de forma controlada después
        de completar la iteración actual.
        
        La notificación a observadores se realiza mediante el patrón Observer,
        invocando automáticamente actualizar() en cada observador registrado.
        
        """
        print("SENSOR: El sensor de humedad ha comenzado a operar.")
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            print(f"SENSOR: Nueva lectura de humedad: {humedad}%")
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def detener(self):
        """
        Señaliza al sensor que debe detener las lecturas de forma controlada.
        
        Activa el Event _detenido, indicando al bucle en run() que debe finalizar
        en su próxima iteración. Este diseño garantiza graceful shutdown, permitiendo
        que el sensor complete su lectura actual y notificación antes de terminar.
        
        No bloquea la ejecución - para esperar la finalización real del hilo, debe
        invocarse join() después de este método, idealmente con un timeout apropiado.
        """
        print("SENSOR: Deteniendo el sensor de humedad.")
        self._detenido.set()

# ==============================================================================
# ARCHIVO 49/68: temperatura_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\riego\sensores\temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de temperatura que realiza lecturas periódicas implementando el patrón Observer.
    
    Este componente es crítico para el sistema de riego automatizado, proporcionando
    datos térmicos en tiempo real que determinan si las condiciones son apropiadas
    para riego. Implementa el patrón Observable para permitir que múltiples componentes
    reaccionen a cambios de temperatura sin acoplamiento directo.
    
    Características del sensor:
    - Rango de medición: -25°C a 50°C (SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)
    - Intervalo de lectura: 2 segundos (INTERVALO_SENSOR_TEMPERATURA)
    - Precisión simulada: 2 decimales
    - Modo de operación: Asíncrono mediante threading

    Attributes:
        _detenido: Event para señalización de detención controlada del hilo.
        _observadores: Lista de observadores heredada de Observable[float].

    """
    
    def __init__(self):
        """
        Inicializa el sensor de temperatura como hilo daemon y observable.
        
        Realiza la inicialización múltiple requerida por herencia múltiple de
        threading.Thread y Observable[float]. El Event _detenido permite
        implementar graceful shutdown del hilo sin forzar terminación abrupta.
        

        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        """
        Simula la lectura del sensor de temperatura ambiental.
        
        Genera un valor aleatorio dentro del rango válido de temperatura definido
        en las constantes del sistema (-25°C a 50°C). En un sistema de producción,
        este método se conectaría a hardware físico como sensores DHT22, DS18B20,
        o similares mediante interfaces GPIO, 1-Wire, o I2C.
        
        La simulación utiliza distribución uniforme para generar valores realistas
        en todo el espectro térmico posible, permitiendo validar el comportamiento
        del sistema bajo condiciones extremas de frío y calor sin requerir hardware
        especializado.
        
        Returns:
            Temperatura ambiental en grados Celsius redondeada a 2 decimales (-25.00 a 50.00).
        
        """
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        """
        Ejecuta el bucle de lectura continua del sensor en segundo plano.
        
        Este método es invocado automáticamente cuando se llama a start() en el hilo.
        Implementa un ciclo infinito que:
        
        1. Lee la temperatura actual mediante _leer_temperatura()
        2. Registra la lectura en consola para trazabilidad y debugging
        3. Notifica el valor a todos los observadores registrados
        4. Espera INTERVALO_SENSOR_TEMPERATURA (2 segundos) antes de la próxima lectura

        """
        print("SENSOR: El sensor de temperatura ha comenzado a operar.")
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            print(f"SENSOR: Nueva lectura de temperatura: {temperatura}°C")
            
            self.notificar_observadores(temperatura)
            
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self):
        """
        Señaliza al sensor que debe detener las lecturas de forma controlada.
        
        Activa el Event _detenido, indicando al bucle en run() que debe finalizar
        en su próxima iteración. Este mecanismo implementa graceful shutdown,
        permitiendo que el sensor complete su lectura actual, notifique a los
        observadores, y finalice limpiamente antes de terminar el hilo.
        
        Este método no bloquea - para esperar la finalización real del hilo, debe
        invocarse join() después de este método, preferiblemente con un timeout
        definido en THREAD_JOIN_TIMEOUT (2.0 segundos).

        """
        print("SENSOR: Deteniendo el sensor de temperatura.")
        self._detenido.set()


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/68: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 51/68: __init__.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/68: arbol_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\arbol_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 53/68: cultivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\cultivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 54/68: cultivo_service_registry.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 55/68: lechuga_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\lechuga_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 56/68: olivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\olivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 57/68: pino_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\pino_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 58/68: zanahoria_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\cultivos\zanahoria_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 59/68: __init__.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 60/68: fincas_service.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\negocio\fincas_service.py
# ==============================================================================

from typing import Dict, Type

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.negocio.paquete import Paquete

class FincasService:
    """
    Servicio de alto nivel para gestión de múltiples fincas forestales.
    
    Orquesta operaciones complejas sobre colecciones de registros forestales,
    coordinando TierraService y PlantacionService.
    
    Implementa las historias de usuario US-018, US-019 y US-020.
    """
    
    def __init__(self):
        """Inicializa el servicio con colección vacía y servicios de dominio."""
        self._registros: Dict[str, RegistroForestal] = {}
        self._plantacion_service = PlantacionService()
        self._tierra_service = TierraService()

    def crear_registro_completo(
        self,
        propietario: str,
        avaluo: float,
        padron_tierra: str,
        superficie_tierra: float,
        domicilio_tierra: str,
        nombre_plantacion: str,
        agua_litros: float
    ) -> RegistroForestal:
        """
        Crea un RegistroForestal completo y lo añade al servicio.
        
        Args:
            propietario: Nombre del propietario.
            avaluo: Valor fiscal de la propiedad.
            padron_tierra: Identificador catastral único.
            superficie_tierra: Superficie en m².
            domicilio_tierra: Ubicación física.
            nombre_plantacion: Nombre de la plantación.
            agua_litros: Agua inicial disponible.
        
        Returns:
            RegistroForestal completo y registrado.
        """
        print(f"\nSERVICIO DE NEGOCIO: Creando registro completo para {propietario}...")
        tierra = self._tierra_service.crear_tierra(
            padron=padron_tierra,
            superficie=superficie_tierra,
            domicilio=domicilio_tierra
        )
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_disponible_m2=tierra.superficie_m2,
            agua_disponible_litros=agua_litros
        )
        registro_completo = RegistroForestal(
            propietario=propietario,
            avaluo_fiscal=avaluo,
            tierra=tierra,
            plantacion=plantacion
        )
        
        self.add_finca(registro_completo)
        print("SERVICIO DE NEGOCIO: Registro completo creado y añadido al servicio.")
        return registro_completo

    def add_finca(self, registro: RegistroForestal):
        """
        Añade un registro forestal a la colección.
        
        Args:
            registro: RegistroForestal a añadir.
        """
        padron = registro.tierra.padron_catastral
        self._registros[padron] = registro
        print(f"FINCAS SERVICE: Se agregó la finca con padrón '{padron}'.")

    def buscar_finca(self, padron: str) -> RegistroForestal:
        """
        Busca un registro forestal por padrón catastral.
        
        Args:
            padron: Identificador catastral a buscar.
        
        Returns:
            RegistroForestal encontrado.
        
        Raises:
            ValueError: Si el padrón no existe.
        """
        registro = self._registros.get(padron)
        if not registro:
            raise ValueError(f"No se encontró ninguna finca con el padrón '{padron}'.")
        return registro

    def fumigar(self, padron: str, plaguicida: str):
        """
        Fumiga una plantación completa.
        
        Args:
            padron: Padrón de la finca a fumigar.
            plaguicida: Tipo de plaguicida a aplicar.
        
        Raises:
            ValueError: Si la finca no existe.
        """
        registro = self.buscar_finca(padron)
        self._plantacion_service.fumigar_plantacion(registro.plantacion, plaguicida)

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[Cultivo]) -> Paquete:
        """
        Cosecha todos los cultivos de un tipo en todas las fincas.
        
        Args:
            tipo_cultivo: Clase del cultivo a cosechar (ej: Pino, Lechuga).
        
        Returns:
            Paquete con todos los cultivos cosechados del tipo especificado.
        """
        nombre_cultivo = tipo_cultivo.__name__
        print(f"\nFINCAS SERVICE: Iniciando cosecha global de '{nombre_cultivo}'...")
        paquete_final = Paquete(f"{nombre_cultivo}s Cosechados Globalmente")

        for registro in self._registros.values():
            plantacion = registro.plantacion
            cultivos_a_cosechar = [c for c in plantacion.cultivos if isinstance(c, tipo_cultivo)]
            
            for cultivo in cultivos_a_cosechar:
                paquete_final.agregar_item(cultivo)
            
            plantacion.cultivos = [c for c in plantacion.cultivos if not isinstance(c, tipo_cultivo)]

        print(f"FINCAS SERVICE: Cosechadas {len(paquete_final.contenido)} unidades de '{nombre_cultivo}'.")
        return paquete_final

# ==============================================================================
# ARCHIVO 61/68: paquete.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\negocio\paquete.py
# ==============================================================================

from typing import List, TypeVar, Generic

T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Contenedor genérico tipo-seguro para empaquetar cultivos cosechados.
    
    Utiliza Generics para garantizar que solo contenga ítems del mismo tipo,
    evitando mezclas accidentales de cultivos diferentes.
    
    Type Parameters:
        T: Tipo de elementos del paquete (ej: Pino, Lechuga).
    
    Attributes:
        nombre_contenido: Descripción textual del contenido.
        contenido: Lista de ítems del tipo T.
    """
    
    def __init__(self, nombre_contenido: str):
        """
        Inicializa un paquete vacío con nombre descriptivo.
        
        Args:
            nombre_contenido: Descripción del contenido a almacenar.
        """
        self.nombre_contenido = nombre_contenido
        self.contenido: List[T] = []

    def agregar_item(self, item: T):
        """
        Agrega un ítem al paquete.
        
        Args:
            item: Elemento del tipo T a agregar.
        """
        self.contenido.append(item)

    def mostrar_contenido(self):
        """
        Muestra el contenido del paquete en formato legible.
        
        Imprime nombre, cantidad de ítems y listado completo.
        Si está vacío, muestra "(Vacío)".
        """
        print(f"\n--- Contenido del Paquete de '{self.nombre_contenido}' ({len(self.contenido)} ítems) ---")
        if not self.contenido:
            print("(Vacío)")
        else:
            for item in self.contenido:
                print(f"- {item}")
        print("-------------------------------------------------")


################################################################################
# DIRECTORIO: servicios\personal
################################################################################

# ==============================================================================
# ARCHIVO 62/68: __init__.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 63/68: trabajador_service.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\personal\trabajador_service.py
# ==============================================================================

from datetime import date

from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """
    Servicio para gestionar operaciones de trabajadores agrícolas.
    
    Centraliza la lógica de negocio relacionada con:
    - Asignación de aptos médicos
    - Validación de aptitud para trabajar
    - Ejecución de tareas asignadas
    
    Implementa las historias de usuario US-015 y US-016.
    """

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str):
        """
        Asigna o actualiza el apto médico de un trabajador.
        
        Args:
            trabajador: Trabajador a actualizar.
            apto: True si está apto, False si no.
            fecha_emision: Fecha de emisión del certificado.
            observaciones: Notas médicas adicionales.
        """
        nuevo_apto = AptoMedico(fecha_emision=fecha_emision, observaciones=observaciones, es_apto=apto)
        trabajador.apto_medico = nuevo_apto
        estado = "APTO" if apto else "NO APTO"
        print(f"SERVICIO: Se asignó apto médico ({estado}) a '{trabajador.nombre}'.")

    def asignar_tarea_si_es_apto(self, trabajador: Trabajador, tarea: Tarea):
        """
        Asigna una tarea solo si el trabajador tiene apto médico vigente.
        
        Args:
            trabajador: Trabajador a asignar tarea.
            tarea: Tarea a asignar.
        """
        if trabajador.puede_trabajar():
            trabajador.asignar_tarea(tarea)
        else:
            print(f"SERVICIO ERROR: El trabajador '{trabajador.nombre}' no tiene apto médico vigente. "
                  f"No se le puede asignar la tarea '{tarea.descripcion}'.")

    def trabajar(self, trabajador: Trabajador, fecha: date, herramienta: Herramienta) -> bool:
        """
        Ejecuta las tareas del trabajador si tiene apto médico válido.
        
        Args:
            trabajador: Trabajador que ejecutará tareas.
            fecha: Fecha de ejecución de tareas.
            herramienta: Herramienta a utilizar.
        
        Returns:
            True si pudo trabajar, False si no tiene apto médico.
        """
        if not trabajador.puede_trabajar():
            print(f"SERVICIO ERROR: {trabajador.nombre} no tiene apto médico vigente y no puede trabajar.")
            return False
        
        print(f"SERVICIO: {trabajador.nombre} comienza a trabajar con la herramienta '{herramienta.nombre}'.")
        trabajador.ejecutar_tareas()
        return True


################################################################################
# DIRECTORIO: servicios\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 64/68: __init__.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/68: plantacion_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\plantacion_service.py
# ==============================================================================

from datetime import date

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class PlantacionService:
    """
    Servicio para operaciones sobre plantaciones agrícolas.
    
    Coordina Factory y Registry para plantar, regar, cosechar y fumigar cultivos.
    Implementa las historias de usuario US-008, US-019 y operaciones de plantación.
    """
    
    def __init__(self):
        """Inicializa el servicio con Factory y Registry de cultivos."""
        self._cultivo_factory = CultivoFactory()
        self._registry = CultivoServiceRegistry()

    def plantar_cultivos_en_lote(self, plantacion: Plantacion, especie: str, cantidad: int):
        """
        Planta múltiples cultivos de la misma especie en la plantación.
        
        Args:
            plantacion: Plantación donde plantar.
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria").
            cantidad: Número de cultivos a plantar.
        
        Raises:
            SuperficieInsuficienteException: Si no hay suficiente superficie.
            ValueError: Si la especie no existe.
        """
        print(f"\nSERVICIO: Intentando plantar un lote de {cantidad} '{especie}'(s) en '{plantacion.nombre}'.")
        for _ in range(cantidad):
            nuevo_cultivo = self._cultivo_factory.crear_cultivo(especie)
            plantacion.plantar_cultivo(nuevo_cultivo)

    def regar_plantacion(self, plantacion: Plantacion):
        """
        Riega todos los cultivos de la plantación.
        
        Consume 10L de agua y distribuye según estrategia de cada cultivo.
        
        Args:
            plantacion: Plantación a regar.
        """
        print(f"\nSERVICIO: Iniciando riego para la plantación '{plantacion.nombre}'.")
        litros_por_riego = 10.0
        
        try:
            plantacion.consumir_agua(litros_por_riego)
            print(f"INFO: La operación de riego consumió {litros_por_riego}L.")
        except Exception as e:
            print(f"ERROR al regar: {e}")
            return

        fecha_actual = date.today()
        for cultivo in plantacion.cultivos:
            litros_calculados = self._registry.absorber_agua(cultivo, fecha_actual)
            cultivo.crecer(litros_calculados)

    def cosechar_plantacion(self, plantacion: Plantacion):
        """
        Cosecha todos los cultivos de la plantación y los empaqueta por tipo.
        
        Args:
            plantacion: Plantación a cosechar.
        """
        print(f"\nSERVICIO: Iniciando cosecha en la plantación '{plantacion.nombre}'.")
        paquetes = {
            "Pino": Paquete("Pinos Cosechados"),
            "Olivo": Paquete("Olivos Cosechados"),
            "Lechuga": Paquete("Lechugas Cosechadas"),
            "Zanahoria": Paquete("Zanahorias Cosechadas")
        }
        servicios = {
            "Pino": PinoService(),
            "Olivo": OlivoService(),
            "Lechuga": LechugaService(),
            "Zanahoria": ZanahoriaService()
        }

        for cultivo in plantacion.cultivos:
            tipo = cultivo.get_tipo()
            if tipo in servicios:
                servicios[tipo].cosechar(cultivo)
                paquetes[tipo].agregar_item(cultivo)
        
        for paquete in paquetes.values():
            paquete.mostrar_contenido()

    def fumigar_plantacion(self, plantacion: Plantacion, plaguicida: str):
        """
        Fumiga todos los cultivos de la plantación con un plaguicida.
        
        Args:
            plantacion: Plantación a fumigar.
            plaguicida: Tipo de plaguicida a aplicar.
        """
        print(f"\nSERVICIO: Fumigando '{plantacion.nombre}' con {plaguicida}.")
        if not plantacion.cultivos:
            print("No hay cultivos que fumigar.")
            return
        print(f"Se han fumigado {len(plantacion.cultivos)} cultivos.")

# ==============================================================================
# ARCHIVO 66/68: registro_forestal_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ==============================================================================

import pickle
import os

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATOS_DEFAULT

class RegistroForestalService:
    """
    Servicio de persistencia para objetos RegistroForestal.
    
    Maneja serialización y deserialización usando Pickle para almacenar
    registros forestales en disco.
    
    Implementa las historias de usuario US-021, US-022 y US-023.
    """
    
    def __init__(self, directorio_datos: str = DIRECTORIO_DATOS_DEFAULT):
        """
        Inicializa el servicio creando el directorio de datos si no existe.
        
        Args:
            directorio_datos: Ruta del directorio para archivos .dat.
        """
        self._directorio_datos = directorio_datos
        os.makedirs(self._directorio_datos, exist_ok=True)

    def persistir(self, registro: RegistroForestal):
        """
        Serializa y guarda un RegistroForestal en archivo .dat.
        
        Args:
            registro: RegistroForestal a persistir.
        
        Raises:
            PersistenciaException: Si falla el guardado.
        """
        nombre_archivo = f"{registro.propietario.replace(' ', '_').lower()}.dat"
        ruta_completa = os.path.join(self._directorio_datos, nombre_archivo)
        
        print(f"\nPERSISTENCIA: Guardando registro para '{registro.propietario}' en '{ruta_completa}'...")
        try:
            with open(ruta_completa, "wb") as f:
                pickle.dump(registro, f)
            print("PERSISTENCIA: Guardado con éxito.")
        except Exception as e:
            raise PersistenciaException(operacion="guardado", causa=e)

    @staticmethod
    def leer_registro(propietario: str, directorio_datos: str = DIRECTORIO_DATOS_DEFAULT) -> RegistroForestal:
        """
        Carga un RegistroForestal desde archivo .dat.
        
        Args:
            propietario: Nombre del propietario (usado como nombre de archivo).
            directorio_datos: Ruta del directorio de datos.
        
        Returns:
            RegistroForestal deserializado.
        
        Raises:
            ValueError: Si propietario es nulo o vacío.
            PersistenciaException: Si falla la lectura o archivo no existe.
        """
        if not propietario or not propietario.strip():
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = f"{propietario.replace(' ', '_').lower()}.dat"
        ruta_completa = os.path.join(directorio_datos, nombre_archivo)
        
        print(f"\nPERSISTENCIA: Cargando registro para '{propietario}' desde '{ruta_completa}'...")
        try:
            with open(ruta_completa, "rb") as f:
                registro = pickle.load(f)
                print("PERSISTENCIA: Carga exitosa.")
                return registro
        except FileNotFoundError as e:
            raise PersistenciaException(operacion="lectura (archivo no encontrado)", causa=e)
        except Exception as e:
            raise PersistenciaException(operacion="lectura", causa=e)

    def mostrar_datos(self, registro: RegistroForestal):
        """
        Muestra los datos del registro en formato legible.
        
        Args:
            registro: RegistroForestal a mostrar.
        """
        registro.mostrar_datos()

# ==============================================================================
# ARCHIVO 67/68: tierra_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\tierra_service.py
# ==============================================================================

from ...entidades.terrenos.tierra import Tierra

class TierraService:
    """
    Servicio para creación y gestión de terrenos catastrales.
    
    Maneja la creación de objetos Tierra con validación de datos.
    """
   
    def crear_tierra(self, padron: str, superficie: float, domicilio: str) -> Tierra:
        """
        Crea una nueva instancia de Tierra con datos catastrales.
        
        Args:
            padron: Identificador único catastral.
            superficie: Superficie en metros cuadrados.
            domicilio: Ubicación física del terreno.
        
        Returns:
            Instancia de Tierra creada.
        """
        print(f"SERVICIO: Creando registro para tierra con padrón {padron}.")
        return Tierra(padron_catastral=padron, superficie_m2=superficie, domicilio=domicilio)


################################################################################
# DIRECTORIO: tests
################################################################################

# ==============================================================================
# ARCHIVO 68/68: tests_casos_especificos.py
# Directorio: tests
# Ruta completa: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\tests\tests_casos_especificos.py
# ==============================================================================

import unittest
import sys
import os
import io
from datetime import date
from unittest.mock import Mock
from contextlib import redirect_stdout

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from main import run as run_main_simulation
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.personal.trabajador import Trabajador, AptoMedico, Tarea, EstadoTarea
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

class TestSistemaCompleto(unittest.TestCase):
    """
    Suite de pruebas de integración para el sistema de gestión forestal.
    
    Valida funcionalidades principales:
    - Ejecución completa del sistema (main.py)
    - Manejo de excepciones (superficie, agua)
    - Gestión de trabajadores con aptos médicos
    - Patrones de diseño (Singleton, Factory)
    
    Cada test es independiente gracias a setUp() y tearDown().
    """

    def setUp(self):
        """
        Configura el entorno antes de cada test.
        
        Inicializa servicios necesarios para las pruebas.
        """
        self.plantacion_service = PlantacionService()
        self.trabajador_service = TrabajadorService()
        self.registry = CultivoServiceRegistry()
        self.factory = CultivoFactory()

    def tearDown(self):
        """
        Limpia archivos generados después de cada test.
        
        Elimina archivos .dat creados durante la ejecución para evitar
        interferencia entre tests.
        """
        file_path = "data/juan_perez.dat"
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_integracion_ejecucion_completa_main(self):
        """
        Valida la ejecución completa del sistema sin errores.
        
        Criterios de éxito:
        - No excepciones no controladas
        - Mensaje de finalización exitosa
        - Archivo de persistencia creado
        """
        print("\n[TEST DE INTEGRACIÓN] Ejecutando simulación completa de main.py...")
        expected_file = "data/juan_perez.dat"
        self.assertFalse(os.path.exists(expected_file), "El archivo de datos ya existía antes del test.")
        
        fake_stdout = io.StringIO()
        with redirect_stdout(fake_stdout):
            try:
                run_main_simulation()
            except Exception as e:
                self.fail(f"La ejecución de main.py falló con una excepción no controlada: {e}")
        
        output = fake_stdout.getvalue()
        self.assertIn("EJEMPLO COMPLETADO EXITOSAMENTE", output)
        self.assertTrue(os.path.exists(expected_file))
        print("[TEST DE INTEGRACIÓN] Simulación completada y validada con éxito.")

    def test_caso1_superficie_insuficiente(self):
        """
        Valida manejo de excepción por superficie insuficiente.
        
        Verifica que el sistema lance SuperficieInsuficienteException
        cuando no hay espacio disponible para plantar.
        """
        plantacion = Plantacion("Test Corto", superficie_disponible_m2=5.0, agua_disponible_litros=1000)
        with self.assertRaises(SuperficieInsuficienteException) as cm:
            self.plantacion_service.plantar_cultivos_en_lote(plantacion, "Pino", 1)
        self.assertGreater(cm.exception.get_superficie_requerida(), cm.exception.get_superficie_disponible())
        print("\n[TEST OK] Caso 1: Superficie Insuficiente validado.")

    def test_caso2_agua_agotada(self):
        """
        Valida manejo de excepción por agua agotada.
        
        Verifica que el sistema lance AguaAgotadaException cuando
        se intenta consumir más agua de la disponible.
        """
        plantacion = Plantacion("Test Seco", superficie_disponible_m2=1000, agua_disponible_litros=3)
        with self.assertRaises(AguaAgotadaException) as cm:
            plantacion.consumir_agua(5)
        self.assertIn("insuficientes", str(cm.exception).lower())
        print("[TEST OK] Caso 2: Agua Agotada validado.")

    def test_caso3_trabajador_sin_apto(self):
        """
        Valida que trabajadores sin apto médico no pueden recibir tareas.
        
        Verifica que el servicio rechaza asignación de tareas a
        trabajadores con apto médico vencido o no apto.
        """
        apto_vencido = AptoMedico(fecha_emision=date(2020, 1, 1), observaciones="Vencido", es_apto=False)
        trabajador_inapto = Trabajador(dni=12345678, nombre="Test Inapto", apto_medico=apto_vencido)
        tarea = Tarea(id_tarea=999, descripcion="Tarea de prueba", fecha_programada=date.today())
        
        self.trabajador_service.asignar_tarea_si_es_apto(trabajador_inapto, tarea)
        
        self.assertEqual(len(trabajador_inapto.tareas), 0)
        print("[TEST OK] Caso 3: Trabajador Sin Apto validado.")

    def test_patron_singleton(self):
        """
        Valida implementación correcta del patrón Singleton.
        
        Verifica que múltiples instancias de CultivoServiceRegistry
        retornan la misma referencia de objeto.
        """
        registry1 = CultivoServiceRegistry()
        registry2 = CultivoServiceRegistry()
        self.assertIs(registry1, registry2)
        print("[TEST OK] Patrón Singleton validado.")

    def test_patron_factory(self):
        """
        Valida implementación correcta del patrón Factory Method.
        
        Verifica:
        - Creación exitosa de cultivos válidos
        - Excepción para especies desconocidas
        """
        pino = self.factory.crear_cultivo("Pino")
        self.assertIsInstance(pino, Pino)
        with self.assertRaises(ValueError):
            self.factory.crear_cultivo("Tomate")
        print("[TEST OK] Patrón Factory validado.")

if __name__ == '__main__':
    unittest.main()


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 68
# Generado: 2025-10-22 08:32:43
################################################################################
