from typing import Dict, Type

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.negocio.paquete import Paquete

class FincasService:
    """
    Servicio de alto nivel para gestión de múltiples fincas forestales.
    
    Orquesta operaciones complejas sobre colecciones de registros forestales,
    coordinando TierraService y PlantacionService.
    
    Implementa las historias de usuario US-018, US-019 y US-020.
    """
    
    def __init__(self):
        """Inicializa el servicio con colección vacía y servicios de dominio."""
        self._registros: Dict[str, RegistroForestal] = {}
        self._plantacion_service = PlantacionService()
        self._tierra_service = TierraService()

    def crear_registro_completo(
        self,
        propietario: str,
        avaluo: float,
        padron_tierra: str,
        superficie_tierra: float,
        domicilio_tierra: str,
        nombre_plantacion: str,
        agua_litros: float
    ) -> RegistroForestal:
        """
        Crea un RegistroForestal completo y lo añade al servicio.
        
        Args:
            propietario: Nombre del propietario.
            avaluo: Valor fiscal de la propiedad.
            padron_tierra: Identificador catastral único.
            superficie_tierra: Superficie en m².
            domicilio_tierra: Ubicación física.
            nombre_plantacion: Nombre de la plantación.
            agua_litros: Agua inicial disponible.
        
        Returns:
            RegistroForestal completo y registrado.
        """
        print(f"\nSERVICIO DE NEGOCIO: Creando registro completo para {propietario}...")
        tierra = self._tierra_service.crear_tierra(
            padron=padron_tierra,
            superficie=superficie_tierra,
            domicilio=domicilio_tierra
        )
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_disponible_m2=tierra.superficie_m2,
            agua_disponible_litros=agua_litros
        )
        registro_completo = RegistroForestal(
            propietario=propietario,
            avaluo_fiscal=avaluo,
            tierra=tierra,
            plantacion=plantacion
        )
        
        self.add_finca(registro_completo)
        print("SERVICIO DE NEGOCIO: Registro completo creado y añadido al servicio.")
        return registro_completo

    def add_finca(self, registro: RegistroForestal):
        """
        Añade un registro forestal a la colección.
        
        Args:
            registro: RegistroForestal a añadir.
        """
        padron = registro.tierra.padron_catastral
        self._registros[padron] = registro
        print(f"FINCAS SERVICE: Se agregó la finca con padrón '{padron}'.")

    def buscar_finca(self, padron: str) -> RegistroForestal:
        """
        Busca un registro forestal por padrón catastral.
        
        Args:
            padron: Identificador catastral a buscar.
        
        Returns:
            RegistroForestal encontrado.
        
        Raises:
            ValueError: Si el padrón no existe.
        """
        registro = self._registros.get(padron)
        if not registro:
            raise ValueError(f"No se encontró ninguna finca con el padrón '{padron}'.")
        return registro

    def fumigar(self, padron: str, plaguicida: str):
        """
        Fumiga una plantación completa.
        
        Args:
            padron: Padrón de la finca a fumigar.
            plaguicida: Tipo de plaguicida a aplicar.
        
        Raises:
            ValueError: Si la finca no existe.
        """
        registro = self.buscar_finca(padron)
        self._plantacion_service.fumigar_plantacion(registro.plantacion, plaguicida)

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[Cultivo]) -> Paquete:
        """
        Cosecha todos los cultivos de un tipo en todas las fincas.
        
        Args:
            tipo_cultivo: Clase del cultivo a cosechar (ej: Pino, Lechuga).
        
        Returns:
            Paquete con todos los cultivos cosechados del tipo especificado.
        """
        nombre_cultivo = tipo_cultivo.__name__
        print(f"\nFINCAS SERVICE: Iniciando cosecha global de '{nombre_cultivo}'...")
        paquete_final = Paquete(f"{nombre_cultivo}s Cosechados Globalmente")

        for registro in self._registros.values():
            plantacion = registro.plantacion
            cultivos_a_cosechar = [c for c in plantacion.cultivos if isinstance(c, tipo_cultivo)]
            
            for cultivo in cultivos_a_cosechar:
                paquete_final.agregar_item(cultivo)
            
            plantacion.cultivos = [c for c in plantacion.cultivos if not isinstance(c, tipo_cultivo)]

        print(f"FINCAS SERVICE: Cosechadas {len(paquete_final.contenido)} unidades de '{nombre_cultivo}'.")
        return paquete_final