class ForestacionException(Exception):
    """
    Excepción base para todos los errores del sistema de forestación.
    
    Clase raíz de la jerarquía de excepciones personalizadas del sistema.
    Todas las excepciones específicas del dominio forestal heredan de esta clase,
    permitiendo un manejo unificado de errores.
    
    Attributes:
        mensaje: Descripción del error ocurrido en el sistema.
    """
    
    def __init__(self, mensaje: str = "Ha ocurrido un error en el sistema de forestación."):
        """
        Inicializa una excepción de forestación con un mensaje descriptivo.
        
        Args:
            mensaje: Descripción del error. Por defecto es un mensaje genérico.
        """
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def get_full_message(self) -> str:
        """
        Obtiene el mensaje completo del error.
        
        Returns:
            Mensaje de error completo como cadena de texto.
        """
        return self.mensaje
