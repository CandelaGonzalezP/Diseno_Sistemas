"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\apto_medico.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\herramienta.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\tarea.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\personal\trabajador.py
# ================================================================================

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

