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