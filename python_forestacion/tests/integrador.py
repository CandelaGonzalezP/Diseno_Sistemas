"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\tests
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: tests_casos_especificos.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\tests\tests_casos_especificos.py
# ================================================================================

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

