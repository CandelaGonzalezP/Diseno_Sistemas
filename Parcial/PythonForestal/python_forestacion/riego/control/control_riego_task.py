import threading
import time
from typing import Optional

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.constantes import (
    TEMP_MIN_RIEGO,  
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO,
    INTERVALO_CONTROL_RIEGO,
    SENSOR_TEMP_MAX
)

class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador automatizado de riego que implementa el patrón Observer.
    
    Opera como un hilo daemon que observa continuamente los sensores de temperatura
    y humedad, evaluando las condiciones ambientales y activando el riego automático
    cuando se cumplen los criterios establecidos.
    
    Este controlador representa el núcleo del sistema de riego inteligente, tomando
    decisiones basadas en datos en tiempo real. Implementa el patrón Observer para
    recibir notificaciones de ambos sensores y el patrón Thread para operar de forma
    asíncrona sin bloquear el resto del sistema.
    
    Condiciones de riego automático:
    - Temperatura entre 8°C y 15°C (TEMP_MIN_RIEGO y TEMP_MAX_RIEGO)
    - Humedad menor a 50% (HUMEDAD_MAX_RIEGO)
    - Ambas condiciones deben cumplirse simultáneamente
    
    El controlador evalúa las condiciones cada 2.5 segundos (INTERVALO_CONTROL_RIEGO)
    y delega la operación de riego al PlantacionService, garantizando separación
    de responsabilidades y mantenibilidad del código.
    
    Attributes:
        _ultima_temperatura: Última lectura de temperatura recibida del sensor (°C).
        _ultima_humedad: Última lectura de humedad recibida del sensor (%).
        _plantacion: Plantación sobre la cual se ejecutará el riego.
        _plantacion_service: Servicio que ejecuta la lógica de riego.
        _detenido: Event para detención controlada del hilo.
    """
    
    def __init__(
        self,
        sensor_temp: TemperaturaReaderTask,
        sensor_hum: HumedadReaderTask,
        plantacion: Plantacion,
        plantacion_service: PlantacionService
    ):
        """
        Inicializa el controlador de riego e inyecta dependencias.
        
        El controlador se registra automáticamente como observador de ambos sensores
        mediante el patrón Observer, garantizando que recibirá notificaciones de
        todas las lecturas realizadas.
        
        Este diseño cumple con Dependency Injection, permitiendo testear el
        controlador con sensores mock y servicios simulados.
        
        Args:
            sensor_temp: Sensor de temperatura (Observable[float]) que notificará lecturas.
            sensor_hum: Sensor de humedad (Observable[float]) que notificará lecturas.
            plantacion: Plantación objetivo donde se ejecutará el riego.
            plantacion_service: Servicio que contiene la lógica de negocio del riego.
        """
        threading.Thread.__init__(self)
        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        
        sensor_temp.agregar_observador(self)
        sensor_hum.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Recibe notificaciones de los sensores e identifica el tipo de lectura.
        
        Implementa el método requerido por la interfaz Observer[float]. Recibe
        valores de temperatura o humedad y los almacena en el estado interno.
        
        La distinción entre temperatura y humedad se realiza mediante análisis
        del rango de valores:
        - Temperatura: valores <= SENSOR_TEMP_MAX (50°C)
        - Humedad: valores > SENSOR_TEMP_MAX (porcentajes hasta 100%)
        
        Este método es llamado automáticamente por los sensores cada vez que
        realizan una lectura, garantizando que el controlador siempre trabaja
        con datos actualizados.
        
        Args:
            evento: Valor numérico de la lectura del sensor (temperatura en °C
                   o humedad en porcentaje).
        
        """
        if evento <= SENSOR_TEMP_MAX: 
             print(f"CONTROLADOR: Notificación de temperatura recibida -> {evento}°C")
             self._ultima_temperatura = evento
        else:
             print(f"CONTROLADOR: Notificación de humedad recibida -> {evento}%")
             self._ultima_humedad = evento

    def _evaluar_condiciones_y_regar(self):
        """
        Evalúa las condiciones ambientales y activa riego si corresponde.
        
        Método privado que contiene la lógica de decisión del sistema de riego
        automatizado. Verifica:
        
        1. Que existan lecturas de ambos sensores (no None)
        2. Que la temperatura esté en el rango óptimo (8°C - 15°C)
        3. Que la humedad sea inferior al umbral (< 50%)
        
        Si todas las condiciones se cumplen, delega la operación de riego al
        PlantacionService. Si no hay agua disponible, captura la excepción
        AguaAgotadaException y registra el error sin detener el sistema.
        
        Este diseño permite que el controlador continúe operando incluso si
        ocurren errores puntuales, garantizando resiliencia del sistema.
        
        Raises:
            No lanza excepciones - las captura internamente para no detener el hilo.
        
        """
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            print("CONTROLADOR: Esperando lecturas iniciales de ambos sensores...")
            return

        print(f"CONTROLADOR: Evaluando T={self._ultima_temperatura}°C, H={self._ultima_humedad}%")
        
        if (TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO and
            self._ultima_humedad < HUMEDAD_MAX_RIEGO):
            print("CONTROLADOR: ¡Condiciones óptimas! Iniciando riego...")
            try:
                self._plantacion_service.regar_plantacion(self._plantacion)
                print("CONTROLADOR: ¡RIEGO COMPLETADO!")
            except Exception as e:
                print(f"CONTROLADOR ERROR: No se pudo regar. Causa: {e}")
        else:
            print("CONTROLADOR: Condiciones no aptas para el riego.")

    def run(self):
        """
        Ejecuta el bucle principal del controlador en segundo plano.
        
        Este método es invocado automáticamente cuando se llama a start() en el hilo.
        Implementa un bucle infinito que evalúa condiciones de riego periódicamente
        cada INTERVALO_CONTROL_RIEGO (2.5 segundos).
        
        El bucle continúa hasta que se invoca detener(), momento en el cual el
        Event _detenido es activado y el bucle termina de forma controlada.
        
        """
        print("CONTROLADOR: El sistema de control de riego ha comenzado a operar.")
        while not self._detenido.is_set():
            self._evaluar_condiciones_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)

    def detener(self):
        """
        Detiene el controlador de forma segura mediante señalización.
        
        Activa el Event _detenido, señalizando al bucle en run() que debe
        finalizar en su próxima iteración. Este diseño garantiza graceful shutdown,
        permitiendo que el hilo complete su operación actual antes de terminar.
        
        Después de invocar este método, se recomienda llamar a join() con timeout
        para esperar la finalización del hilo:
        
        """
        print("CONTROLADOR: Deteniendo el sistema de control de riego.")
        self._detenido.set()