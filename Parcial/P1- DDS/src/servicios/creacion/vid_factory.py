from entidades.cultivos.vid import Vid, Malbec, CabernetSauvignon

class VidFactory:
    def crear_vid(self, varietal: str) -> Vid:
        if varietal.lower() == "malbec":
            return Malbec()
        elif varietal.lower() == "cabernet sauvignon":
            return CabernetSauvignon()
        else:
            raise ValueError(f"Varietal '{varietal}' no disponible.")