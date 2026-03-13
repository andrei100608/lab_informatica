from GenericItem import GenericItem

class NormalItem(GenericItem):
    
    def __init__(self,nome,prezzo) -> None:
        super().__init(nome,prezzo)