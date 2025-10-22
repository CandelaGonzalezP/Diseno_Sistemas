class MensajesException:
    """
    Clase de utilidad que centraliza mensajes de error del sistema.
    
    Define constantes con mensajes de error estandarizados para garantizar
    consistencia en los mensajes mostrados al usuario. Los mensajes utilizan
    formato de cadena para permitir interpolación de valores dinámicos.
    
    Attributes:
        ESPECIE_DESCONOCIDA: Mensaje cuando se intenta crear un cultivo de especie no reconocida.
        SERVICIO_NO_REGISTRADO: Mensaje cuando no existe servicio para un tipo de cultivo.
        PADRON_DUPLICADO: Mensaje cuando se intenta registrar un padrón catastral duplicado.
    """
   
    ESPECIE_DESCONOCIDA = "Especie de cultivo desconocida: '{}'"
    """Mensaje de error para especie de cultivo no reconocida. Requiere 1 parámetro: nombre de especie."""
    
    SERVICIO_NO_REGISTRADO = "No hay un servicio registrado para el cultivo: '{}'"
    """Mensaje de error para cultivo sin servicio registrado. Requiere 1 parámetro: tipo de cultivo."""
    
    PADRON_DUPLICADO = "El padrón catastral '{}' ya existe en el sistema."
    """Mensaje de error para padrón catastral duplicado. Requiere 1 parámetro: número de padrón."""