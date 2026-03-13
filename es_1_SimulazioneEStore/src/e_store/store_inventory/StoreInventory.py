
from e_store.store_item.GenericItem import GenericItem  
class StoreInventory:

    def __init__(self) -> None:
        self.oggetti=dict()
        

    def aggiungi_oggetto(self, oggetto : GenericItem, quantita) -> int:
        if oggetto not in self.oggetti:
            self.oggetti[oggetto]=quantita
        else:
            self.oggetti[oggetto]+=quantita
        
        return self.oggetti[oggetto]
        

    def rimuovi_oggetto(self, oggetto : GenericItem, quantita) -> int:
        if oggetto in self.oggetti and quantita<=self.oggetti[oggetto]:
            self.oggetti[oggetto]-=quantita
            return True
        return False
            
    
