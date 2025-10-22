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