import sys
import os

# Añade la carpeta 'src' al path de Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Las importaciones ahora son directas desde las carpetas de dominio
from entidades.organizacion.inv import INV
from servicios.creacion.finca_builder import FincaBuilder
from servicios.creacion.vid_factory import VidFactory
from servicios.personal.contratista import Contratista
from servicios.negocio.estrategias_cosecha import CosechaMecanica

if __name__ == "__main__":
    print("--- SIMULACIÓN DE COSECHA EN MENDOZA CON PATRONES DE DISEÑO ---")

    # 1. Singleton: Obtenemos la instancia única del INV
    inv = INV()

    # 2. Builder: Construimos dos fincas
    finca_lujan = (FincaBuilder(hectareas=50)
                   .con_nombre("Finca Luján de Cuyo")
                   .con_tipo_suelo("Aluvial")
                   .build())

    finca_maipu = (FincaBuilder(hectareas=120)
                   .con_nombre("Finca Maipú")
                   .build())

    # 3. Observer: El INV se suscribe a las notificaciones de ambas fincas
    finca_lujan.attach(inv)
    finca_maipu.attach(inv)

    # 4. Factory: Creamos vides y las plantamos
    fabrica_vides = VidFactory()
    malbec = fabrica_vides.crear_vid("malbec")
    cabernet = fabrica_vides.crear_vid("cabernet sauvignon")
    finca_lujan.plantar_vid(malbec)
    finca_maipu.plantar_vid(cabernet)

    # 5. Strategy: Un contratista realiza la cosecha
    contratista_perez = Contratista("Pérez")

    # Usa la estrategia por defecto (Manual) en la primera finca
    contratista_perez.ejecutar_cosecha(finca_lujan)

    # Cambia a una estrategia mecánica para la finca más grande
    contratista_perez.set_estrategia(CosechaMecanica())
    contratista_perez.ejecutar_cosecha(finca_maipu)

    print("\n--- SIMULACIÓN FINALIZADA ---")