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