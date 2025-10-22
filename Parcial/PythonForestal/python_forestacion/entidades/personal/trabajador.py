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