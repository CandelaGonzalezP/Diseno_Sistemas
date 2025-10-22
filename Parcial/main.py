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