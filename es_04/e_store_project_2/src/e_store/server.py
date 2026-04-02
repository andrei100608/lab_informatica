from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional, List
from e_store.store.store import Store
from e_store.customer.promotional_customer import PromotionalCustomer
from e_store.store_item.normal_item import NormalItem
from e_store.store_item.foreign_item import ForeignItem
from e_store.customer.generic_customer import GenericCustomer


app = FastAPI(title="E-Store API")

store = Store(1000)
store.inventory.add_item(NormalItem("Laptop", 500), 5)
store.inventory.add_item(ForeignItem("Smartphone", 800), 3)


users: Dict[str, GenericCustomer] = {
    "Alice": PromotionalCustomer("Alice", 1000, "password123"),
    "Bob": PromotionalCustomer("Bob", 800, "bob123"),
}


class InventoryItem(BaseModel):
    name: str
    quantity: int
    price: float

class UserItem(BaseModel):
    name: str
    quantity: int

class ItemInfo(BaseModel):
    name: str
    quantity: int
    price: float

class UserBalance(BaseModel):
    username: str
    balance: float

class PurchaseRequest(BaseModel):
    username: str
    password: str
    item_name: str
    quantity: int

class PurchaseResponse(BaseModel):
    success: bool
    message: str
    new_balance: Optional[float] = None

@app.get("/inventory")
def get_inventory() -> List[InventoryItem]:
    inventory_items: List[InventoryItem] =[]
    for name, data in store.inventory.get_items().items():
        inventory_items.append(InventoryItem(name=name, quantity=data["quantity"], price= data["item"].get_price()))
    return inventory_items


@app.get("/user/{username}/items")
def get_user_items(username : str) -> List[UserItem]:
    
    if username in users:
        user_items: List[UserItem]= []
        customer = users[username]
        for item_name, quantity in customer.items.items():
            user_items.append(UserItem(name=item_name, quantity=quantity))
        return user_items
    else:
        raise HTTPException(status_code=404, detail=f"Utente {username} non trovato")
    
        
@app.get("/item/{item}")
def get_item_information(item: str) -> ItemInfo:
    if item not in store.inventory.get_items():
        raise HTTPException(status_code=404, detail=f"Item {item} non trovato")

    valore = store.inventory.get_items()[item]
    return ItemInfo(name = item, quantity=valore["quantity"],price=valore["item"].get_price())
    
@app.get("/user/{username}/balance")
def get_balance(username: str) -> UserBalance:
    if username not in users:
        raise HTTPException(status_code=404, detail=f"Utente {username} non trovato")
    customer = users[username]
    return UserBalance(username=username,balance=customer.balance)

@app.post("/purchase")
def purchase(purchase_req: PurchaseRequest)->PurchaseResponse:
    nome = purchase_req.username

    if nome not in users or purchase_req.password != users[nome].password:
        return PurchaseResponse(success=False,message="Username o password non corretti")
    if purchase_req.item_name not in store.inventory.get_items():
        return PurchaseResponse(success=False,message=f"Item {purchase_req.tem_name} non disponibile nel negozio")
    
    if (store.sell_item(users[nome],purchase_req.item_name,purchase_req.quantity)):
        return PurchaseResponse(success= True,message="acquisto effettuato",new_balance=users[nome].balance)
    elif (users[nome].balance < store.inventory.get_items()[purchase_req.item_name]["item"].get_price()*purchase_req.quantity):
        return PurchaseResponse(success=False,message=f"credito insufficiente: {users[nome].balance}")
    else:
        return PurchaseResponse(success=False,message="oggetti non disponibili")
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)