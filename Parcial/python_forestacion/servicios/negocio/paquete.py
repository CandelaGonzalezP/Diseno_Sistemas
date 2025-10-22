from typing import List, TypeVar, Generic

T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Contenedor genérico tipo-seguro para empaquetar cultivos cosechados.
    
    Utiliza Generics para garantizar que solo contenga ítems del mismo tipo,
    evitando mezclas accidentales de cultivos diferentes.
    
    Type Parameters:
        T: Tipo de elementos del paquete (ej: Pino, Lechuga).
    
    Attributes:
        nombre_contenido: Descripción textual del contenido.
        contenido: Lista de ítems del tipo T.
    """
    
    def __init__(self, nombre_contenido: str):
        """
        Inicializa un paquete vacío con nombre descriptivo.
        
        Args:
            nombre_contenido: Descripción del contenido a almacenar.
        """
        self.nombre_contenido = nombre_contenido
        self.contenido: List[T] = []

    def agregar_item(self, item: T):
        """
        Agrega un ítem al paquete.
        
        Args:
            item: Elemento del tipo T a agregar.
        """
        self.contenido.append(item)

    def mostrar_contenido(self):
        """
        Muestra el contenido del paquete en formato legible.
        
        Imprime nombre, cantidad de ítems y listado completo.
        Si está vacío, muestra "(Vacío)".
        """
        print(f"\n--- Contenido del Paquete de '{self.nombre_contenido}' ({len(self.contenido)} ítems) ---")
        if not self.contenido:
            print("(Vacío)")
        else:
            for item in self.contenido:
                print(f"- {item}")
        print("-------------------------------------------------")