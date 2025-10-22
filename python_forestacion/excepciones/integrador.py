"""
Archivo integrador generado automaticamente
Directorio: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones
Fecha: 2025-10-22 08:32:43
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

from .forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua para completar una operación.
    
    Se utiliza cuando se intenta realizar un riego u otra operación que requiere
    agua, pero la plantación no tiene suficientes recursos hídricos disponibles.
    Proporciona información detallada sobre la cantidad requerida versus la disponible.
    
    Attributes:
        _requerida: Cantidad de agua necesaria para la operación en litros.
        _disponible: Cantidad de agua actualmente disponible en litros.
    """
    
    def __init__(self, agua_requerida: float, agua_disponible: float):
        """
        Inicializa una excepción de agua agotada con cantidades específicas.
        
        Args:
            agua_requerida: Cantidad de agua necesaria en litros.
            agua_disponible: Cantidad de agua disponible en litros.
        """
        self._requerida = agua_requerida
        self._disponible = agua_disponible
       
        mensaje = (f"Recursos hídricos insuficientes. Requerido: {self._requerida:.2f}L, "
                   f"Disponible: {self._disponible:.2f}L.")
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Returns:
            Mensaje amigable indicando falta de agua.
        """
        return "Agua insuficiente para completar el riego."

    def get_agua_requerida(self) -> float:
        """
        Obtiene la cantidad de agua que se requería para la operación.
        
        Returns:
            Cantidad de agua requerida en litros.
        """
        return self._requerida

    def get_agua_disponible(self) -> float:
        """
        Obtiene la cantidad de agua actualmente disponible.
        
        Returns:
            Cantidad de agua disponible en litros.
        """
        return self._disponible


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

class ForestacionException(Exception):
    """
    Excepción base para todos los errores del sistema de forestación.
    
    Clase raíz de la jerarquía de excepciones personalizadas del dominio forestal.
    Todas las excepciones específicas (SuperficieInsuficienteException,
    AguaAgotadaException, PersistenciaException) heredan de esta clase,
    permitiendo un manejo unificado de errores mediante catch polimórfico.
    
    Esta excepción implementa separación de mensajes:
    - Usuario: Mensaje simplificado y amigable
    - Técnico: Mensaje detallado con contexto técnico
    
    Attributes:
        mensaje: Descripción completa del error (mensaje técnico).
    
    
    """
    
    def __init__(self, mensaje: str = "Ha ocurrido un error en el sistema de forestación."):
        """
        Inicializa una excepción de forestación con mensaje descriptivo.
        
        Args:
            mensaje: Descripción técnica del error. Por defecto es un mensaje genérico.
        """
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def get_full_message(self) -> str:
        """
        Obtiene el mensaje técnico completo del error.
        
        Proporciona información detallada para logs, debugging y diagnóstico técnico.
        
        Returns:
            Mensaje de error completo como cadena de texto.

        """
        return self.mensaje

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: C:\Users\cande\OneDrive\Documentos\candela\TERCER AÑO\SEGUNDO SEM\Repo_DDS\Diseno_Sistemas\.\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie para plantar un cultivo.
    
    Se utiliza cuando se intenta plantar un cultivo pero la plantación no tiene
    suficiente superficie disponible. Proporciona información detallada sobre:
    - Superficie requerida por el cultivo
    - Superficie disponible en la plantación
    - Diferencia (déficit de superficie)
    
    Esta excepción cumple con el criterio de aceptación de US-004 que especifica:
    "Si no hay superficie, lanzar SuperficieInsuficienteException".
    
    Attributes:
        _requerida: Superficie necesaria para el cultivo en metros cuadrados.
        _disponible: Superficie actualmente disponible en metros cuadrados.
 

    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa una excepción de superficie insuficiente con valores específicos.
        
        Construye mensajes técnicos detallados incluyendo las cantidades exactas
        de superficie requerida versus disponible para facilitar el diagnóstico.
        
        Args:
            superficie_requerida: Superficie necesaria en metros cuadrados (debe ser > 0).
            superficie_disponible: Superficie disponible en metros cuadrados (debe ser >= 0).

        """
        self._requerida = superficie_requerida
        self._disponible = superficie_disponible
       
        mensaje = (
            f"Superficie insuficiente. "
            f"Requerido: {self._requerida:.2f} m², "
            f"Disponible: {self._disponible:.2f} m². "
            f"Déficit: {(self._requerida - self._disponible):.2f} m²"
        )
        super().__init__(mensaje)

    def get_user_message(self) -> str:
        """
        Obtiene un mensaje simplificado para mostrar al usuario final.
        
        Proporciona un mensaje amigable sin detalles técnicos para
        interfaces de usuario o reportes orientados a usuarios no técnicos.
        
        Returns:
            Mensaje simplificado indicando falta de superficie.
  
        """
        return "Superficie insuficiente para plantar."

    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie que se requería para plantar el cultivo.
        
        Útil para cálculos de expansión o re-planificación de plantaciones.
        
        Returns:
            Superficie requerida en metros cuadrados.
   
        """
        return self._requerida

    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie actualmente disponible en la plantación.
        
        Permite al código cliente tomar decisiones sobre cuántos cultivos
        alternativos podrían plantarse con la superficie disponible.
        
        Returns:
            Superficie disponible en metros cuadrados.

        """
        return self._disponible
    
    def get_deficit(self) -> float:
        """
        Calcula el déficit de superficie (cuánto falta).
        
        Returns:
            Diferencia entre requerido y disponible en metros cuadrados.
  
        """
        return self._requerida - self._disponible

