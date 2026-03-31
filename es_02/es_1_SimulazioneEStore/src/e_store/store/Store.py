from e_store.store_inventory.StoreInventory import StoreInventory
from e_store.store_item.GenericItem import GenericItem 
from e_store.customer.GenericCustomer import GenericCustomer 
from e_store.customer.PromotionalCustomer import PromotionalCustomer
from e_store.customer.NormalCustomer import NormalCustomer

class Store:

    def __init__(self, cash) -> None:
        self.inventory=StoreInventory()
        self.cash=cash
        self.customers=[]
        
    def compra_oggetti(self, oggetto : GenericItem, quantita) -> int:
        if quantita*oggetto.prezzo<=self.cash:
            self.cash-=quantita*oggetto.prezzo
            self.inventory.aggiungi_oggetto(oggetto,quantita)
            return quantita*oggetto.prezzo
        return 0
    
    ''' imput: oggetto e quantita deisdera      output: prezzo al quale si è venduto senno 0'''
    def vende_oggetti(self, oggetto : GenericItem, quantita, customer : GenericCustomer ) -> int:
        
        prezzo=oggetto.prezzo*quantita
        if customer.__class__ == PromotionalCustomer:
            prezzo*=0.95
        print(prezzo)
        print(customer.denaro)
        if customer.denaro>=prezzo and self.inventory.rimuovi_oggetto(oggetto,quantita):
            print("comprati")
            self.cash+=prezzo
            customer.denaro-=prezzo
            return prezzo
        return 0
    
    def vende_oggetti_by_nome(self, nome, quantita,customer) ->int:
        for key in self.inventory.oggetti:
            if key.nome==nome:
                return self.vende_oggetti(key, quantita, customer)
        return 0
                
    def crea_utente(self, nome,denaro, password, tipo): 
        if tipo=="promotional":
            self.customers.append(PromotionalCustomer(nome,denaro,password))
        else:
            self.customers.append(NormalCustomer(nome,denaro,password))

    def accredita_denaro(self,nome,password,importo):
        for customer in self.customers:
            if customer.password==password and customer.nome==nome:
                customer.denaro+=importo
                return customer.denaro

    def autentica_utente(self, nome, password) -> GenericCustomer:
        for customer in self.customers:
            if customer.password==password and customer.nome==nome:
                return customer
        return None
    
    def show_inventory(self):
        for oggetto in self.inventory.oggetti:
            print(oggetto,str(self.inventory.oggetti[oggetto]))

