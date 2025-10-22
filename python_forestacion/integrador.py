"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: constantes.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\constantes.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: main.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\main.py
# ================================================================================

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

