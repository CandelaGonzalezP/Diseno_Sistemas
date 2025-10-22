"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\personal
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\personal\trabajador_service.py
# ================================================================================

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

