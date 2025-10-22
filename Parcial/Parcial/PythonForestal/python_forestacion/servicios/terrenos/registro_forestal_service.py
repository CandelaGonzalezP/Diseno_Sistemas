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