from abc import ABC, abstractmethod

class Vid(ABC):
    @abstractmethod
    def get_varietal(self) -> str:
        pass

    def __str__(self):
        return f"Vid de varietal '{self.get_varietal()}'"

class Malbec(Vid):
    def get_varietal(self) -> str:
        return "Malbec"

class CabernetSauvignon(Vid):
    def get_varietal(self) -> str:
        return "Cabernet Sauvignon"