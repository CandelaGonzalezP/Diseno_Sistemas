from .forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepción lanzada cuando ocurre un error durante operaciones de persistencia.
    
    Se utiliza para encapsular errores que ocurren durante la serialización,
    deserialización o cualquier operación de E/S relacionada con el almacenamiento
    de datos en disco. Mantiene referencia a la causa original del error para
    facilitar el diagnóstico.
    
    Attributes:
        _operacion: Tipo de operación que falló (ej. "ESCRITURA", "LECTURA").
        _causa: Excepción original que causó el error de persistencia.
    """
    
    def __init__(self, operacion: str, causa: Exception):
        """
        Inicializa una excepción de persistencia con contexto del error.
        
        Args:
            operacion: Nombre de la operación que falló (ej. "ESCRITURA", "LECTURA").
            causa: Excepción original que causó el fallo.
        """
        self._operacion = operacion
        self._causa = causa
       
        mensaje = f"Error durante la operación de persistencia '{self._operacion}'. Causa: {self._causa}"
        super().__init__(mensaje)
       
    def get_operacion(self) -> str:
        """
        Obtiene el tipo de operación de persistencia que falló.
        
        Returns:
            Nombre de la operación (ej. "ESCRITURA", "LECTURA").
        """
        return self._operacion
       
    def get_causa_original(self) -> Exception:
        """
        Obtiene la excepción original que causó el error.
        
        Permite acceder a la excepción subyacente (ej. IOError, PickleError)
        para obtener más detalles sobre el fallo.
        
        Returns:
            Excepción original que causó el error de persistencia.
        """
        return self._causa
