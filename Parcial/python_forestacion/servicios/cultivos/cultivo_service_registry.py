from threading import Lock
from datetime import date

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_CONSTANTE_HORTALIZAS
)

class CultivoServiceRegistry:
    """
    Registro centralizado implementando patrones Singleton y Registry.
    
    Proporciona punto único de acceso para operaciones sobre cultivos mediante
    dispatch polimórfico, eliminando cascadas de isinstance().
    
    Operaciones soportadas:
    - Absorción de agua (estacional para árboles, constante para hortalizas)
    - Visualización de datos específicos por tipo
    
    Singleton thread-safe con double-checked locking.
    
    Attributes:
        _instance: Instancia única compartida.
        _lock: Lock para thread-safety.
        _absorber_agua_handlers: Handlers de absorción por tipo.
        _mostrar_datos_handlers: Handlers de visualización por tipo.
        _initialized: Flag de inicialización única.
    """
    
    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Garantiza Singleton thread-safe mediante double-checked locking.
        
        Returns:
            La instancia única de CultivoServiceRegistry.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Inicializa handlers solo en la primera instanciación.
        
        Registra handlers de absorción y visualización para cada tipo de cultivo.
        El flag _initialized evita reinicialización en llamadas posteriores.
        """
        if hasattr(self, '_initialized'):
            return
        
        print("INFO: Inicializando Registry y handlers.")
        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_arbol_seasonal,
            Olivo: self._absorber_agua_arbol_seasonal,
            Lechuga: self._absorber_agua_hortaliza_constante,
            Zanahoria: self._absorber_agua_hortaliza_constante
        }
        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }
        self._initialized = True

    def _absorber_agua_arbol_seasonal(self, cultivo: Cultivo, fecha: date) -> int:
        """
        Handler de absorción estacional para árboles.
        
        Args:
            cultivo: Árbol a evaluar.
            fecha: Fecha para determinar estación.
        
        Returns:
            5L si verano (junio-agosto), 2L si invierno.
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO

    def _absorber_agua_hortaliza_constante(self, cultivo: Cultivo, fecha: date) -> int:
        """
        Handler de absorción constante para hortalizas.
        
        Args:
            cultivo: Hortaliza a evaluar.
            fecha: No utilizada en absorción constante.
        
        Returns:
            Cantidad fija definida en constantes.
        """
        return ABSORCION_CONSTANTE_HORTALIZAS

    def _mostrar_datos_pino(self, pino: Pino):
        """
        Muestra datos específicos de Pino.
        
        Args:
            pino: Instancia a visualizar.
        """
        print(f"Cultivo: {pino.get_tipo()}")
        print(f"Superficie: {pino.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {pino.litros_agua_absorbidos} L")
        print(f"Altura: {pino.altura_metros:.2f} m")
        print(f"Variedad: {pino.variedad}")

    def _mostrar_datos_olivo(self, olivo: Olivo):
        """
        Muestra datos específicos de Olivo.
        
        Args:
            olivo: Instancia a visualizar.
        """
        print(f"Cultivo: {olivo.get_tipo()}")
        print(f"Superficie: {olivo.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {olivo.litros_agua_absorbidos} L")
        print(f"Altura: {olivo.altura_metros:.2f} m")
        print(f"Tipo de aceituna: {olivo.tipo_aceituna.name}")

    def _mostrar_datos_lechuga(self, lechuga: Lechuga):
        """
        Muestra datos específicos de Lechuga.
        
        Args:
            lechuga: Instancia a visualizar.
        """
        print(f"Cultivo: {lechuga.get_tipo()}")
        print(f"Superficie: {lechuga.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {lechuga.litros_agua_absorbidos} L")
        print(f"Variedad: {lechuga.variedad}")
        print(f"Invernadero: True")

    def _mostrar_datos_zanahoria(self, zanahoria: Zanahoria):
        """
        Muestra datos específicos de Zanahoria.
        
        Args:
            zanahoria: Instancia a visualizar.
        """
        print(f"Cultivo: {zanahoria.get_tipo()}")
        print(f"Superficie: {zanahoria.metros_cuadrados_requeridos} m²")
        print(f"Agua almacenada: {zanahoria.litros_agua_absorbidos} L")
        print(f"Es baby carrot: {zanahoria.es_baby}")

    def absorber_agua(self, cultivo: Cultivo, fecha_actual: date) -> int:
        """
        Despacha absorción al handler correcto mediante Registry.
        
        Args:
            cultivo: Cultivo que absorberá agua.
            fecha_actual: Fecha para cálculos estacionales.
        
        Returns:
            Litros absorbidos según tipo y estrategia.
        
        Raises:
            TypeError: Si no existe handler para el tipo.
        """
        tipo_cultivo = type(cultivo)
        handler = self._absorber_agua_handlers.get(tipo_cultivo)
        if not handler:
            raise TypeError(f"No hay un handler de absorción de agua para '{tipo_cultivo.__name__}'")
        return handler(cultivo, fecha_actual)

    def mostrar_datos(self, cultivo: Cultivo):
        """
        Despacha visualización al handler correcto mediante Registry.
        
        Args:
            cultivo: Cultivo a visualizar.
        
        Raises:
            TypeError: Si no existe handler para el tipo.
        """
        print("-" * 20)
        tipo_cultivo = type(cultivo)
        handler = self._mostrar_datos_handlers.get(tipo_cultivo)
        if not handler:
            raise TypeError(f"No hay un handler para mostrar datos de '{tipo_cultivo.__name__}'")
        handler(cultivo)