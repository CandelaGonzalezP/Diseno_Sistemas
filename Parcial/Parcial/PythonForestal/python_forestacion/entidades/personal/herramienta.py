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