from abc import ABC,abstractmethod

class Player(ABC):

    def __init__(self,nome="local") -> None:
        super().__init__()
        self.nome = nome

    @abstractmethod
    def genera_numero(self):
        pass
