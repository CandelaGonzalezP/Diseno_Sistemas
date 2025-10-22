import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)

class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de humedad que realiza lecturas periódicas implementando el patrón Observer.

    Características del sensor:
    - Rango de medición: 0% a 100% (SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)
    - Intervalo de lectura: 3 segundos (INTERVALO_SENSOR_HUMEDAD)
    - Precisión simulada: 2 decimales
    - Modo de operación: Asíncrono mediante threading
    
    Attributes:
        _detenido: Event para señalización de detención controlada del hilo.
        _observadores: Lista de observadores heredada de Observable[float].
    
    """
    
    def __init__(self):
        """
        Inicializa el sensor de humedad como hilo daemon y observable.
        
        Realiza la inicialización múltiple requerida por herencia múltiple de
        threading.Thread y Observable[float]. El Event _detenido permite
        implementar graceful shutdown del hilo.
        
        El sensor comienza sin observadores registrados; estos deben agregarse
        mediante agregar_observador() antes de iniciar el hilo para recibir
        notificaciones.
        
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        """
        Simula la lectura del sensor de humedad ambiental.
        
        Genera un valor aleatorio dentro del rango válido de humedad definido
        en las constantes del sistema (0% a 100%). En un sistema real, este
        método se conectaría a hardware físico mediante GPIO, I2C, o protocolos
        similares.
        
        La simulación utiliza distribución uniforme para generar valores
        realistas en todo el rango posible, permitiendo probar el sistema
        con diversos escenarios de humedad sin necesidad de hardware real.
        
        Returns:
            Porcentaje de humedad ambiental redondeado a 2 decimales (0.00 - 100.00).

        """
        return round(random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX), 2)

    def run(self):
        """
        Ejecuta el bucle de lectura continua del sensor en segundo plano.
        
        Este método es invocado automáticamente cuando se llama a start() en el hilo.
        Implementa un ciclo infinito que:
        
        1. Lee el valor actual de humedad mediante _leer_humedad()
        2. Registra la lectura en consola para trazabilidad
        3. Notifica el valor a todos los observadores registrados
        4. Espera INTERVALO_SENSOR_HUMEDAD (3 segundos) antes de la próxima lectura
        
        El ciclo continúa hasta que se invoca detener(), momento en el cual el
        Event _detenido es activado y el bucle termina de forma controlada después
        de completar la iteración actual.
        
        La notificación a observadores se realiza mediante el patrón Observer,
        invocando automáticamente actualizar() en cada observador registrado.
        
        """
        print("SENSOR: El sensor de humedad ha comenzado a operar.")
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            print(f"SENSOR: Nueva lectura de humedad: {humedad}%")
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def detener(self):
        """
        Señaliza al sensor que debe detener las lecturas de forma controlada.
        
        Activa el Event _detenido, indicando al bucle en run() que debe finalizar
        en su próxima iteración. Este diseño garantiza graceful shutdown, permitiendo
        que el sensor complete su lectura actual y notificación antes de terminar.
        
        No bloquea la ejecución - para esperar la finalización real del hilo, debe
        invocarse join() después de este método, idealmente con un timeout apropiado.
        """
        print("SENSOR: Deteniendo el sensor de humedad.")
        self._detenido.set()