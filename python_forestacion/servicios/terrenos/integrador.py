"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

from datetime import date

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class PlantacionService:
    """
    Servicio para operaciones sobre plantaciones agrícolas.
    
    Coordina Factory y Registry para plantar, regar, cosechar y fumigar cultivos.
    Implementa las historias de usuario US-008, US-019 y operaciones de plantación.
    """
    
    def __init__(self):
        """Inicializa el servicio con Factory y Registry de cultivos."""
        self._cultivo_factory = CultivoFactory()
        self._registry = CultivoServiceRegistry()

    def plantar_cultivos_en_lote(self, plantacion: Plantacion, especie: str, cantidad: int):
        """
        Planta múltiples cultivos de la misma especie en la plantación.
        
        Args:
            plantacion: Plantación donde plantar.
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria").
            cantidad: Número de cultivos a plantar.
        
        Raises:
            SuperficieInsuficienteException: Si no hay suficiente superficie.
            ValueError: Si la especie no existe.
        """
        print(f"\nSERVICIO: Intentando plantar un lote de {cantidad} '{especie}'(s) en '{plantacion.nombre}'.")
        for _ in range(cantidad):
            nuevo_cultivo = self._cultivo_factory.crear_cultivo(especie)
            plantacion.plantar_cultivo(nuevo_cultivo)

    def regar_plantacion(self, plantacion: Plantacion):
        """
        Riega todos los cultivos de la plantación.
        
        Consume 10L de agua y distribuye según estrategia de cada cultivo.
        
        Args:
            plantacion: Plantación a regar.
        """
        print(f"\nSERVICIO: Iniciando riego para la plantación '{plantacion.nombre}'.")
        litros_por_riego = 10.0
        
        try:
            plantacion.consumir_agua(litros_por_riego)
            print(f"INFO: La operación de riego consumió {litros_por_riego}L.")
        except Exception as e:
            print(f"ERROR al regar: {e}")
            return

        fecha_actual = date.today()
        for cultivo in plantacion.cultivos:
            litros_calculados = self._registry.absorber_agua(cultivo, fecha_actual)
            cultivo.crecer(litros_calculados)

    def cosechar_plantacion(self, plantacion: Plantacion):
        """
        Cosecha todos los cultivos de la plantación y los empaqueta por tipo.
        
        Args:
            plantacion: Plantación a cosechar.
        """
        print(f"\nSERVICIO: Iniciando cosecha en la plantación '{plantacion.nombre}'.")
        paquetes = {
            "Pino": Paquete("Pinos Cosechados"),
            "Olivo": Paquete("Olivos Cosechados"),
            "Lechuga": Paquete("Lechugas Cosechadas"),
            "Zanahoria": Paquete("Zanahorias Cosechadas")
        }
        servicios = {
            "Pino": PinoService(),
            "Olivo": OlivoService(),
            "Lechuga": LechugaService(),
            "Zanahoria": ZanahoriaService()
        }

        for cultivo in plantacion.cultivos:
            tipo = cultivo.get_tipo()
            if tipo in servicios:
                servicios[tipo].cosechar(cultivo)
                paquetes[tipo].agregar_item(cultivo)
        
        for paquete in paquetes.values():
            paquete.mostrar_contenido()

    def fumigar_plantacion(self, plantacion: Plantacion, plaguicida: str):
        """
        Fumiga todos los cultivos de la plantación con un plaguicida.
        
        Args:
            plantacion: Plantación a fumigar.
            plaguicida: Tipo de plaguicida a aplicar.
        """
        print(f"\nSERVICIO: Fumigando '{plantacion.nombre}' con {plaguicida}.")
        if not plantacion.cultivos:
            print("No hay cultivos que fumigar.")
            return
        print(f"Se han fumigado {len(plantacion.cultivos)} cultivos.")

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

import pickle
import os

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATOS_DEFAULT

class RegistroForestalService:
    """
    Servicio de persistencia para objetos RegistroForestal.
    
    Maneja serialización y deserialización usando Pickle para almacenar
    registros forestales en disco.
    
    Implementa las historias de usuario US-021, US-022 y US-023.
    """
    
    def __init__(self, directorio_datos: str = DIRECTORIO_DATOS_DEFAULT):
        """
        Inicializa el servicio creando el directorio de datos si no existe.
        
        Args:
            directorio_datos: Ruta del directorio para archivos .dat.
        """
        self._directorio_datos = directorio_datos
        os.makedirs(self._directorio_datos, exist_ok=True)

    def persistir(self, registro: RegistroForestal):
        """
        Serializa y guarda un RegistroForestal en archivo .dat.
        
        Args:
            registro: RegistroForestal a persistir.
        
        Raises:
            PersistenciaException: Si falla el guardado.
        """
        nombre_archivo = f"{registro.propietario.replace(' ', '_').lower()}.dat"
        ruta_completa = os.path.join(self._directorio_datos, nombre_archivo)
        
        print(f"\nPERSISTENCIA: Guardando registro para '{registro.propietario}' en '{ruta_completa}'...")
        try:
            with open(ruta_completa, "wb") as f:
                pickle.dump(registro, f)
            print("PERSISTENCIA: Guardado con éxito.")
        except Exception as e:
            raise PersistenciaException(operacion="guardado", causa=e)

    @staticmethod
    def leer_registro(propietario: str, directorio_datos: str = DIRECTORIO_DATOS_DEFAULT) -> RegistroForestal:
        """
        Carga un RegistroForestal desde archivo .dat.
        
        Args:
            propietario: Nombre del propietario (usado como nombre de archivo).
            directorio_datos: Ruta del directorio de datos.
        
        Returns:
            RegistroForestal deserializado.
        
        Raises:
            ValueError: Si propietario es nulo o vacío.
            PersistenciaException: Si falla la lectura o archivo no existe.
        """
        if not propietario or not propietario.strip():
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = f"{propietario.replace(' ', '_').lower()}.dat"
        ruta_completa = os.path.join(directorio_datos, nombre_archivo)
        
        print(f"\nPERSISTENCIA: Cargando registro para '{propietario}' desde '{ruta_completa}'...")
        try:
            with open(ruta_completa, "rb") as f:
                registro = pickle.load(f)
                print("PERSISTENCIA: Carga exitosa.")
                return registro
        except FileNotFoundError as e:
            raise PersistenciaException(operacion="lectura (archivo no encontrado)", causa=e)
        except Exception as e:
            raise PersistenciaException(operacion="lectura", causa=e)

    def mostrar_datos(self, registro: RegistroForestal):
        """
        Muestra los datos del registro en formato legible.
        
        Args:
            registro: RegistroForestal a mostrar.
        """
        registro.mostrar_datos()

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

from ...entidades.terrenos.tierra import Tierra

class TierraService:
    """
    Servicio para creación y gestión de terrenos catastrales.
    
    Maneja la creación de objetos Tierra con validación de datos.
    """
   
    def crear_tierra(self, padron: str, superficie: float, domicilio: str) -> Tierra:
        """
        Crea una nueva instancia de Tierra con datos catastrales.
        
        Args:
            padron: Identificador único catastral.
            superficie: Superficie en metros cuadrados.
            domicilio: Ubicación física del terreno.
        
        Returns:
            Instancia de Tierra creada.
        """
        print(f"SERVICIO: Creando registro para tierra con padrón {padron}.")
        return Tierra(padron_catastral=padron, superficie_m2=superficie, domicilio=domicilio)

