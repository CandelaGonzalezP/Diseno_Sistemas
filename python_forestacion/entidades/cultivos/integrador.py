"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

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


