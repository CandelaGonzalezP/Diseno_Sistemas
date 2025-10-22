# ==============================================================================
# ESTRATEGIA SEASONAL
# ==============================================================================
MES_INICIO_VERANO = 6
MES_FIN_VERANO = 8
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2

# ==============================================================================
# CARACTERÍSTICAS DE CULTIVOS 
# ==============================================================================
SUPERFICIE_PINO_M2 = 10.0
CRECIMIENTO_PINO_POR_RIEGO_M = 0.10
SUPERFICIE_OLIVO_M2 = 15.0
CRECIMIENTO_OLIVO_POR_RIEGO_M = 0.01
SUPERFICIE_LECHUGA_M2 = 0.5
SUPERFICIE_ZANAHORIA_M2 = 0.3
ABSORCION_CONSTANTE_HORTALIZAS = 2

# ==============================================================================
# SISTEMA DE RIEGO 
# ==============================================================================
TEMP_MIN_RIEGO = 8.0
TEMP_MAX_RIEGO = 15.0
HUMEDAD_MAX_RIEGO = 50.0
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5

SENSOR_TEMP_MIN = -25.0
SENSOR_TEMP_MAX = 50.0
SENSOR_HUMEDAD_MIN = 0.0
SENSOR_HUMEDAD_MAX = 100.0

THREAD_JOIN_TIMEOUT = 2.0

# ==============================================================================
# PERSISTENCIA 
# ==============================================================================
DIRECTORIO_DATOS_DEFAULT = "data""""
Constantes centralizadas del sistema de gestión forestal.

Agrupa todos los valores mágicos del sistema en un único archivo para facilitar
mantenimiento y configuración. Organizado por categorías funcionales.

Principio DRY (Don't Repeat Yourself): Ningún valor debe estar hardcodeado
en el código - todos deben referenciarse desde este módulo.
"""

# ==============================================================================
# ESTRATEGIA SEASONAL
# ==============================================================================
MES_INICIO_VERANO = 6
"""Mes de inicio del verano en el hemisferio sur (junio)."""

MES_FIN_VERANO = 8
"""Mes de fin del verano en el hemisferio sur (agosto)."""

ABSORCION_SEASONAL_VERANO = 5
"""Litros absorbidos por árboles durante el verano."""

ABSORCION_SEASONAL_INVIERNO = 2
"""Litros absorbidos por árboles durante el invierno."""

# ==============================================================================
# CARACTERÍSTICAS DE CULTIVOS 
# ==============================================================================
SUPERFICIE_PINO_M2 = 10.0
"""Superficie requerida por cada pino en metros cuadrados."""

CRECIMIENTO_PINO_POR_RIEGO_M = 0.10
"""Incremento de altura del pino por cada riego en metros."""

SUPERFICIE_OLIVO_M2 = 15.0
"""Superficie requerida por cada olivo en metros cuadrados."""

CRECIMIENTO_OLIVO_POR_RIEGO_M = 0.01
"""Incremento de altura del olivo por cada riego en metros."""

SUPERFICIE_LECHUGA_M2 = 0.5
"""Superficie requerida por cada lechuga en metros cuadrados."""

SUPERFICIE_ZANAHORIA_M2 = 0.3
"""Superficie requerida por cada zanahoria en metros cuadrados."""

ABSORCION_CONSTANTE_HORTALIZAS = 2
"""Litros absorbidos por hortalizas en cada riego (valor constante)."""

# ==============================================================================
# SISTEMA DE RIEGO 
# ==============================================================================
TEMP_MIN_RIEGO = 8.0
"""Temperatura mínima en °C para activar riego automático."""

TEMP_MAX_RIEGO = 15.0
"""Temperatura máxima en °C para activar riego automático."""

HUMEDAD_MAX_RIEGO = 50.0
"""Humedad máxima en % para activar riego automático."""

INTERVALO_SENSOR_TEMPERATURA = 2.0
"""Intervalo de lectura del sensor de temperatura en segundos."""

INTERVALO_SENSOR_HUMEDAD = 3.0
"""Intervalo de lectura del sensor de humedad en segundos."""

INTERVALO_CONTROL_RIEGO = 2.5
"""Intervalo de evaluación del controlador de riego en segundos."""

# --- RANGOS DE VALORES DE SENSORES ---
SENSOR_TEMP_MIN = -25.0
"""Temperatura mínima simulada por el sensor en °C."""

SENSOR_TEMP_MAX = 50.0
"""Temperatura máxima simulada por el sensor en °C."""

SENSOR_HUMEDAD_MIN = 0.0
"""Humedad mínima simulada por el sensor en %."""

SENSOR_HUMEDAD_MAX = 100.0
"""Humedad máxima simulada por el sensor en %."""

THREAD_JOIN_TIMEOUT = 2.0
"""Timeout para esperar finalización de threads en segundos."""

# ==============================================================================
# PERSISTENCIA 
# ==============================================================================
DIRECTORIO_DATOS_DEFAULT = "data"
"""Directorio por defecto para almacenar archivos .dat de registros forestales."""