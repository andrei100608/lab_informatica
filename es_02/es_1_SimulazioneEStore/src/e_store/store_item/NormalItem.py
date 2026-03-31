from e_store.store_item.GenericItem import GenericItem

class NormalItem(GenericItem):
    
    def __init__(self,nome,prezzo) -> None:
        super().__init__(nome,prezzo)