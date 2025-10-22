import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de temperatura que realiza lecturas periódicas implementando el patrón Observer.
    
    Este componente es crítico para el sistema de riego automatizado, proporcionando
    datos térmicos en tiempo real que determinan si las condiciones son apropiadas
    para riego. Implementa el patrón Observable para permitir que múltiples componentes
    reaccionen a cambios de temperatura sin acoplamiento directo.
    
    Características del sensor:
    - Rango de medición: -25°C a 50°C (SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)
    - Intervalo de lectura: 2 segundos (INTERVALO_SENSOR_TEMPERATURA)
    - Precisión simulada: 2 decimales
    - Modo de operación: Asíncrono mediante threading

    Attributes:
        _detenido: Event para señalización de detención controlada del hilo.
        _observadores: Lista de observadores heredada de Observable[float].

    """
    
    def __init__(self):
        """
        Inicializa el sensor de temperatura como hilo daemon y observable.
        
        Realiza la inicialización múltiple requerida por herencia múltiple de
        threading.Thread y Observable[float]. El Event _detenido permite
        implementar graceful shutdown del hilo sin forzar terminación abrupta.
        

        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        """
        Simula la lectura del sensor de temperatura ambiental.
        
        Genera un valor aleatorio dentro del rango válido de temperatura definido
        en las constantes del sistema (-25°C a 50°C). En un sistema de producción,
        este método se conectaría a hardware físico como sensores DHT22, DS18B20,
        o similares mediante interfaces GPIO, 1-Wire, o I2C.
        
        La simulación utiliza distribución uniforme para generar valores realistas
        en todo el espectro térmico posible, permitiendo validar el comportamiento
        del sistema bajo condiciones extremas de frío y calor sin requerir hardware
        especializado.
        
        Returns:
            Temperatura ambiental en grados Celsius redondeada a 2 decimales (-25.00 a 50.00).
        
        """
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        """
        Ejecuta el bucle de lectura continua del sensor en segundo plano.
        
        Este método es invocado automáticamente cuando se llama a start() en el hilo.
        Implementa un ciclo infinito que:
        
        1. Lee la temperatura actual mediante _leer_temperatura()
        2. Registra la lectura en consola para trazabilidad y debugging
        3. Notifica el valor a todos los observadores registrados
        4. Espera INTERVALO_SENSOR_TEMPERATURA (2 segundos) antes de la próxima lectura

        """
        print("SENSOR: El sensor de temperatura ha comenzado a operar.")
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            print(f"SENSOR: Nueva lectura de temperatura: {temperatura}°C")
            
            self.notificar_observadores(temperatura)
            
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self):
        """
        Señaliza al sensor que debe detener las lecturas de forma controlada.
        
        Activa el Event _detenido, indicando al bucle en run() que debe finalizar
        en su próxima iteración. Este mecanismo implementa graceful shutdown,
        permitiendo que el sensor complete su lectura actual, notifique a los
        observadores, y finalice limpiamente antes de terminar el hilo.
        
        Este método no bloquea - para esperar la finalización real del hilo, debe
        invocarse join() después de este método, preferiblemente con un timeout
        definido en THREAD_JOIN_TIMEOUT (2.0 segundos).

        """
        print("SENSOR: Deteniendo el sensor de temperatura.")
        self._detenido.set()