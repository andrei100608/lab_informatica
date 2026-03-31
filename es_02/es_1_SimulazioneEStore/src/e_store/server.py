from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional, List
from e_store.store.Store import Store
from e_store.store_item.NormalItem import NormalItem
from e_store.store_item.ForeignItem import ForeignItem
from e_store.customer.GenericCustomer import GenericCustomer
from e_store.customer.PromotionalCustomer import PromotionalCustomer

app = FastAPI(title="E-Store API")

store = Store(1000)
store.compra_oggetti(NormalItem("Laptop", 500), 5)
store.compra_oggetti(ForeignItem("Smartphone", 800), 3)

users: Dict[str, GenericCustomer] = {
    "Alice": PromotionalCustomer("Alice", 1000, "password123"),
    "Bob": PromotionalCustomer("Bob", 800, "bob123"),
}

class InventoryItem(BaseModel):
    name: str
    quantity: int
    price: float



@app.get("/inventory")
def get_inventory() -> List[InventoryItem]:
    lista: List[InventoryItem] = []
    for item,quantity in store.inventory.get_items().items():
        lista.append(InventoryItem(name = item.nome,quantity=quantity,price = item.prezzo))

    return lista


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)