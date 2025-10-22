"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\terrenos\tierra.py
# ================================================================================

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


