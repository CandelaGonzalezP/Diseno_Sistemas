from typing import Dict, Callable, Any
from ...entidades.cultivos.cultivo import Cultivo
from ...entidades.cultivos.pino import Pino
from ...entidades.cultivos.olivo import Olivo
from ...entidades.cultivos.lechuga import Lechuga
from ...entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    """Implementa el patrón Factory Method para crear instancias de cultivos.

    Esta clase centraliza la lógica de creación de diferentes tipos de cultivos,
    desacoplando el resto de la aplicación de las clases concretas.
    Utiliza un diccionario de 'factories' para un despacho eficiente y extensible.

    Attributes:
        _factories (Dict[str, Callable[..., Cultivo]]): Un diccionario estático
            que mapea el nombre de una especie a una función que crea
            una instancia de esa especie.
    """
    _factories: Dict[str, Callable[..., Cultivo]] = {
        "pino": lambda: Pino(),
        "olivo": lambda: Olivo(),
        "lechuga": lambda: Lechuga(),
        "zanahoria": lambda: Zanahoria()
    }

    @staticmethod
    def crear_cultivo(especie: str, **kwargs: Any) -> Cultivo:
        """Crea una instancia de un cultivo a partir de su especie.

        Este método estático actúa como el punto de entrada de la fábrica.
        Busca la especie solicitada en el registro de fábricas y, si la
        encuentra, ejecuta la función de creación correspondiente.

        Args:
            especie (str): El nombre del cultivo a crear (ej. "Pino").
                No es sensible a mayúsculas/minúsculas.
            **kwargs (Any): Argumentos opcionales de palabra clave que se
                pasarían al constructor del cultivo si fuera necesario.
                Actualmente no se utiliza pero se incluye para extensibilidad.

        Returns:
            Cultivo: Una instancia del cultivo solicitado, que hereda de la
                clase base Cultivo.

        Raises:
            ValueError: Si la especie solicitada no se encuentra en el
                registro de fábricas.
        """
        especie = especie.lower()
        if especie not in CultivoFactory._factories:
            raise ValueError(f"Especie de cultivo desconocida: '{especie}'")

        return CultivoFactory._factories[especie]()