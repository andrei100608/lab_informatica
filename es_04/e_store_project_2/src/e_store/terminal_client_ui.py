import requests

BASE_URL = "http://127.0.0.1:8000"

def get_inventory() -> None:
    print("store inventory")
    response = requests.get(f"{BASE_URL}/inventory")

    #controllo status code
    if response.status_code == 200:
        content_type = response.headers.get("Content-Type", "")

        # verifica che sia json
        if "application/json" in content_type:
            try:
                prodotti = response.json()
                for prodotto in prodotti:
                    print(f"{prodotto['name']}: {prodotto['quantity']} available at {prodotto['price']} each")
            except ValueError:
                print("Errore: la risposta non è un JSON valido")
        else:
            print("Errore: la risposta non è json")
            print("content-type:", content_type)
    else:
        print("Errore HTTP:", response.status_code)
    
def get_balance(username: str) -> float:
    response = requests.get(f"{BASE_URL}/user/{username}/balance")

    if response.status_code == 200:
        content_type = response.headers.get("Content-Type", "")

        # verifica che sia json
        if "application/json" in content_type:
            try:
                balance = response.json()
                return balance['balance']
            except ValueError:
                print("Errore: la risposta non è un JSON valido")
        else:
            print("Errore: la risposta non è json")
            print("content-type:", content_type)
    else:
        print("Errore HTTP:", response.status_code)

def make_purchase(username: str,password: str,item_name: str, quantity: int) -> None:
    payload = {"username":username, 
               "password":password, 
               "item_name":item_name,
               "quantity":quantity}
    
    response = requests.post(f"{BASE_URL}/purchase",json=payload)

    if response.status_code == 200:
        try:
            data = response.json()
            if (data['success']):
                print("Purchase successful!")
                print(data['message'],data['new_balance'])
            else:
                print("Purchase failed")
                print(data['message'])
        except ValueError:
            print("Errore: la risposta non è un JSON valido")


def run_client() -> None:
    print("Welcome to the E-Store Client!")
    username = input("Inserisci username: ")
    password = input("Inserisci password: ")

    while True:
        print("Your balance:",get_balance(username))
        get_inventory()

        choice = input("Scegli cosa fare (purchase o quit): ")
        if choice == 'quit':
            print("Arrivederci")
            break
        if choice == 'purchase':
            prodotto = input('inserisci nome prodotto: ')
            try:
                quantity = int(input("inserisci quantità: "))
            except:
                print("Invalid quantity. Please enter a number.")
                continue
            make_purchase(username,password,prodotto,quantity)

if __name__ == "__main__":
    run_client()